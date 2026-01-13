#!/usr/bin/env python3
"""
Python Vocabulary Census

Extract vocabulary frequency statistics from Python projects
for Rosetta Map allocation reference.
"""

import ast
import json
import keyword
import builtins
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
from typing import Optional
import argparse


# =============================================================================
# Word Classifier
# =============================================================================

BUILTIN_NAMES = set(dir(builtins))


def classify_word(word: str) -> str:
    """
    Classify word into: keyword, builtin, magic, identifier, string_constant
    """
    if keyword.iskeyword(word):
        return "keyword"
    if word in BUILTIN_NAMES:
        return "builtin"
    if word.startswith("__") and word.endswith("__"):
        return "magic"
    return "identifier"


# =============================================================================
# AST Extractor
# =============================================================================

class VocabularyExtractor(ast.NodeVisitor):
    """
    Extract vocabulary from Python AST
    
    Extracted node types:
    - ast.Name: variable/function name references
    - ast.FunctionDef: function definition names
    - ast.ClassDef: class definition names
    - ast.Attribute: attribute access
    - ast.Constant (str): string constants
    - ast.Import / ast.ImportFrom: module names
    - ast.keyword: keyword arguments
    - ast.Call.func.attr: decorator calls
    - ast.annotation: type annotations
    """
    
    def __init__(self):
        self.vocabulary: list[dict] = []
        self._in_docstring_position = False
    
    def _add_word(self, word: str, word_type: str):
        """Add word (applying filter rules)"""
        # Filter: exclude single chars and pure digits
        if len(word) < 2:
            return
        if word.isdigit():
            return
        
        self.vocabulary.append({
            "word": word,
            "type": word_type
        })
    
    def visit_Name(self, node: ast.Name):
        word_type = classify_word(node.id)
        self._add_word(node.id, word_type)
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node: ast.FunctionDef):
        word_type = "magic" if node.name.startswith("__") else "identifier"
        self._add_word(node.name, word_type)
        
        # Extract type annotations
        for arg in node.args.args:
            if arg.annotation:
                self._extract_annotation(arg.annotation)
        if node.returns:
            self._extract_annotation(node.returns)
        
        # Skip docstring
        self.generic_visit(node)
    
    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.visit_FunctionDef(node)  # Reuse logic
    
    def visit_ClassDef(self, node: ast.ClassDef):
        self._add_word(node.name, "identifier")
        self.generic_visit(node)
    
    def visit_Attribute(self, node: ast.Attribute):
        self._add_word(node.attr, "identifier")
        self.generic_visit(node)
    
    def visit_Constant(self, node: ast.Constant):
        # Only extract string constants, exclude docstrings
        if isinstance(node.value, str) and len(node.value) >= 2:
            # Simple filter: exclude long or multi-line (usually docstrings)
            if len(node.value) <= 50 and "\n" not in node.value:
                # Validate string is properly encodable (skip surrogate chars)
                try:
                    node.value.encode('utf-8')
                    self._add_word(node.value, "string_constant")
                except UnicodeEncodeError:
                    pass  # Skip invalid strings
        self.generic_visit(node)
    
    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            module = alias.name.split(".")[0]  # Only top-level module
            self._add_word(module, "identifier")
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module:
            module = node.module.split(".")[0]
            self._add_word(module, "identifier")
        self.generic_visit(node)
    
    def visit_keyword(self, node: ast.keyword):
        if node.arg:
            self._add_word(node.arg, "identifier")
        self.generic_visit(node)
    
    def visit_Call(self, node: ast.Call):
        # Extract decorator calls: @app.route -> route
        if isinstance(node.func, ast.Attribute):
            self._add_word(node.func.attr, "identifier")
        self.generic_visit(node)
    
    def _extract_annotation(self, node: ast.expr):
        """Extract identifiers from type annotations"""
        if isinstance(node, ast.Name):
            self._add_word(node.id, classify_word(node.id))
        elif isinstance(node, ast.Subscript):
            self._extract_annotation(node.value)
            if isinstance(node.slice, ast.Tuple):
                for elt in node.slice.elts:
                    self._extract_annotation(elt)
            else:
                self._extract_annotation(node.slice)
        elif isinstance(node, ast.Attribute):
            self._add_word(node.attr, "identifier")


def extract_from_source(source_code: str) -> list[dict]:
    """Extract vocabulary from source code"""
    try:
        tree = ast.parse(source_code)
        extractor = VocabularyExtractor()
        extractor.visit(tree)
        return extractor.vocabulary
    except SyntaxError:
        return []


def extract_from_file(file_path: Path) -> list[dict]:
    """Extract vocabulary from file"""
    try:
        source = file_path.read_text(encoding="utf-8", errors="ignore")
        return extract_from_source(source)
    except Exception:
        return []


# =============================================================================
# Project Analyzer
# =============================================================================

def analyze_project(project_path: Path) -> dict:
    """
    Analyze entire project and return vocabulary statistics
    """
    vocab_counter = defaultdict(lambda: {"count": 0, "type": None})
    total_files = 0
    total_lines = 0
    parsed_files = 0
    failed_files = 0
    errors = []
    
    py_files = list(project_path.rglob("*.py"))
    total_files = len(py_files)
    
    for py_file in py_files:
        try:
            source = py_file.read_text(encoding="utf-8", errors="ignore")
            total_lines += source.count("\n") + 1
            
            vocab = extract_from_source(source)
            if vocab:
                parsed_files += 1
                for item in vocab:
                    key = (item["word"], item["type"])
                    vocab_counter[key]["count"] += 1
                    vocab_counter[key]["type"] = item["type"]
            else:
                failed_files += 1
        except Exception as e:
            failed_files += 1
            errors.append({
                "file": str(py_file.relative_to(project_path)),
                "reason": str(e)
            })
    
    # Convert to list format
    vocabulary = [
        {"word": word, "count": data["count"], "type": data["type"]}
        for (word, type_), data in sorted(
            vocab_counter.items(),
            key=lambda x: -x[1]["count"]
        )
    ]
    
    return {
        "stats": {
            "total_files": total_files,
            "total_lines": total_lines,
            "parsed_files": parsed_files,
            "failed_files": failed_files
        },
        "vocabulary": vocabulary,
        "errors": errors[:10]  # Keep only first 10 errors
    }


# =============================================================================
# Aggregator
# =============================================================================

def aggregate_reports(project_reports: list[dict]) -> dict:
    """
    Aggregate vocabulary statistics from multiple projects
    
    Dedup key: (word, type)
    """
    global_vocab = defaultdict(lambda: {
        "global_count": 0,
        "project_coverage": 0,
        "type": None
    })
    
    for report in project_reports:
        seen_in_project = set()
        for item in report.get("vocabulary", []):
            key = (item["word"], item["type"])
            global_vocab[key]["global_count"] += item["count"]
            global_vocab[key]["type"] = item["type"]
            
            if key not in seen_in_project:
                global_vocab[key]["project_coverage"] += 1
                seen_in_project.add(key)
    
    # Convert to list, sorted by global count
    # Filter: only include words with global_count > 2
    vocabulary = [
        {
            "word": word,
            "global_count": data["global_count"],
            "project_coverage": data["project_coverage"],
            "type": data["type"]
        }
        for (word, type_), data in sorted(
            global_vocab.items(),
            key=lambda x: -x[1]["global_count"]
        )
        if data["global_count"] > 2
    ]
    
    return {
        "meta": {
            "version": "0.0.0.1",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "tool_version": "vocab-census v0.1.0",
            "source_projects": len(project_reports),
            "total_unique_words": len(vocabulary)
        },
        "vocabulary": vocabulary
    }


# =============================================================================
# Main Entry
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Python Vocabulary Census")
    parser.add_argument("command", choices=["analyze", "aggregate"], 
                        help="Command to run")
    parser.add_argument("target", nargs="?", help="Project path or pattern")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--lock-file", help="Use lock file for reproducibility")
    
    args = parser.parse_args()
    
    if args.command == "analyze":
        if not args.target:
            print("Error: Please specify a project path")
            return 1
        
        project_path = Path(args.target)
        if not project_path.exists():
            print(f"Error: Path not found: {project_path}")
            return 1
        
        print(f"Analyzing {project_path}...")
        result = analyze_project(project_path)
        result["project"] = {
            "name": project_path.name,
            "path": str(project_path)
        }
        
        output_path = args.output or f"output/projects/{project_path.name}.json"
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"Done! Found {len(result['vocabulary'])} unique words")
        print(f"Output: {output_path}")
    
    elif args.command == "aggregate":
        projects_dir = Path("output/projects")
        if not projects_dir.exists():
            print("Error: No project reports found in output/projects/")
            return 1
        
        reports = []
        for json_file in projects_dir.glob("*.json"):
            with open(json_file, encoding="utf-8") as f:
                reports.append(json.load(f))
        
        if not reports:
            print("Error: No project reports to aggregate")
            return 1
        
        print(f"Aggregating {len(reports)} project reports...")
        result = aggregate_reports(reports)
        
        output_path = args.output or "output/vocab_report.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        # Output CSV files
        csv_full_path = output_path.replace(".json", ".csv")
        csv_preview_path = output_path.replace(".json", "_preview.csv")
        
        def write_csv(f, vocab_items, meta):
            """Write CSV with meta comments header"""
            f.write(f'# version: {meta["version"]}\n')
            f.write(f'# generated_at: {meta["generated_at"]}\n')
            f.write(f'# tool_version: {meta["tool_version"]}\n')
            f.write(f'# source_projects: {meta["source_projects"]}\n')
            f.write(f'# total_unique_words: {meta["total_unique_words"]}\n')
            f.write("word,global_count,project_coverage,type\n")
            for item in vocab_items:
                word = item["word"].replace('"', '""')
                if "," in word or '"' in word or "\n" in word:
                    word = f'"{word}"'
                f.write(f'{word},{item["global_count"]},{item["project_coverage"]},{item["type"]}\n')
        
        # Write full CSV
        with open(csv_full_path, "w", encoding="utf-8") as f:
            write_csv(f, result["vocabulary"], result["meta"])
        
        # Compress full CSV to tar.gz
        import tarfile
        tar_path = csv_full_path + ".tar.gz"
        with tarfile.open(tar_path, "w:gz") as tar:
            tar.add(csv_full_path, arcname="vocab_report.csv")
        
        # Write preview CSV (top 1000 words for GitHub preview)
        preview_meta = result["meta"].copy()
        preview_meta["note"] = "preview (top 1000 words)"
        with open(csv_preview_path, "w", encoding="utf-8") as f:
            f.write(f'# note: preview (top 1000 words, see vocab_report.csv.tar.gz for full data)\n')
            write_csv(f, result["vocabulary"][:1000], preview_meta)
        
        # Remove uncompressed full CSV (keep only tar.gz)
        Path(csv_full_path).unlink()
        
        # Calculate hash
        content = json.dumps(result, ensure_ascii=False, sort_keys=True)
        content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        
        print(f"Done! Total {result['meta']['total_unique_words']} unique words")
        print(f"Output: {output_path}")
        print(f"Output: {tar_path} (full data)")
        print(f"Output: {csv_preview_path} (top 1000 for preview)")
        print(f"Hash: {content_hash}")
    
    return 0


if __name__ == "__main__":
    exit(main())
