# Contributing to Project LOGOS
## 为 Project LOGOS 做贡献

> **"Come, join us. Help us write the Global Rosetta Map."**

Thank you for your interest in contributing to Project LOGOS! This document explains how to participate in building the Semantic Compute Architecture for a Type-II Civilization.

---

## 🌍 Ways to Contribute

### 1. Rosetta Map Contributions (推荐)
Help build the **Global Rosetta Map** — the dictionary for human-machine communication.

**What you can submit:**
- New Semantic IDs for your domain (finance, healthcare, gaming, etc.)
- Translations and aliases for existing IDs
- Corrections to existing mappings

**Process:**
1. Check if the concept already exists in [rosetta-map/](./rosetta-map/)
2. Open an Issue with `[Rosetta]` prefix
3. Propose your ID using the template below
4. Community review (7-day window)
5. Merge into the canonical map

### 2. RFC Contributions
Propose or improve technical specifications.

**Areas:**
- V.O.I.D. architecture enhancements
- New Atom layouts for specialized use cases
- SCP instruction set proposals

### 3. Documentation
Improve explanations, add tutorials, fix typos.

### 4. Reference Implementation
Contribute to the SCP emulator or Velo runtime (separate repositories).

---

## 📝 Rosetta ID Proposal Template

```markdown
## Rosetta ID Proposal

**Concept**: [Full English name]
**Chinese**: [中文名称]
**Proposed Alias**: [7-char max, following VSCP rules]
**Tier**: [0-Axioms / 1-WebNet / 2-Business / 3-Commons]

### Justification
- **Frequency**: [How often is this used in code/data?]
- **Uniqueness**: [Why can't an existing ID cover this?]
- **Universality**: [Is this concept global or domain-specific?]

### Examples
```python
# Show how this ID would be used
atom = Atom.from_id("your_alias")
```
```

---

## ✅ VSCP Naming Rules (ID 命名规则)

All Rosetta aliases must follow the **Velo Standard Contraction Protocol**:

| Priority | Rule | Example |
|----------|------|---------|
| **L1** | Golden Intuition: Use as-is if ≤7 chars | `config` → `config` |
| **L2** | Smart Numeronym: Prefix(3) + Count + Suffix(1) | `transaction` → `trx7n` |
| **L3** | Compound Skeleton: First consonants of each part | `content-type` → `cnt-typ` |
| **L4** | Vowel Drop: Remove non-leading vowels | `message` → `msg` |

**Charset**: `[a-z0-9_-]` only. No uppercase.

---

## 🔄 PR Review Process

1. **Automated Checks**
   - Alias length ≤7 characters
   - Charset compliance
   - No ID collisions

2. **Community Review (7 days)**
   - At least 2 approvals from different language communities
   - No blocking objections

3. **Maintainer Merge**
   - Final review by core team
   - Assignment of canonical ID number

---

## 🌐 Language Community Representatives

To ensure **Data Neutrality**, we seek representatives from each major language community:

| Language | Status | Representative |
|----------|--------|----------------|
| English | ✅ Active | Core Team |
| 中文 (Chinese) | ✅ Active | Core Team |
| 日本語 (Japanese) | 🔍 Seeking | — |
| 한국어 (Korean) | 🔍 Seeking | — |
| Español | 🔍 Seeking | — |
| العربية (Arabic) | 🔍 Seeking | — |

**Interested?** Open an Issue with `[Language Rep]` prefix.

---

## 📜 Licensing

By contributing, you agree that your contributions will be released under:

- **Specifications & Rosetta Map**: [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/) (Public Domain)
- **Code**: [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

This ensures the Rosetta Map remains **humanity's shared resource**, not owned by any corporation.

---

## 🤝 Code of Conduct

- **Respect all cultures**: The Rosetta Map represents human civilization, not any single culture.
- **Data Neutrality**: Chinese `钱` and English `Money` are equally valid; neither subsumes the other.
- **Good Faith**: Assume contributors have good intentions.

---

## 📞 Contact

- **Issues**: [GitHub Issues](../../issues)
- **Discussions**: [GitHub Discussions](../../discussions)

---

> **"Let us teach silicon-based life what LOGOS truly means."**
