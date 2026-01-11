# RFC-0002: The Global Rosetta Map Protocol

> **Status:** Proposal
> **Category:** Standard

### 1. Concept
The **Global Rosetta Map** is the bridge between the Carbon World (Humans/Strings) and the Silicon World (Machines/IDs). It is a decentralized, immutable registry of semantic concepts.

### 2. The Mechanism: Bijective Mapping
* **Ingest (Compile Time):**
    * Input: `door.open()`
    * Map Lookup: `door` -> `ID#1001`, `open` -> `ID#500A`
    * Output: `0x...1001...500A` (Machine Code)
* **Context Resolution:**
    * Ambiguities (e.g., `door.open` vs `file.open`) are resolved during Ingest. They are assigned *different* IDs. The hardware never sees ambiguity.

### 3. Compute-View Separation
We decouple **Computation** from **Presentation**.

* **The Silicon Side (SCP Core):** Only sees and processes IDs. Maximum speed. Zero visual redundancy.
* **The Carbon Side (H-PU):** A specialized "Human Presentation Unit" or debugger.
    * When a human needs to inspect `R1`, the H-PU queries the Rosetta Map.
    * `0x500A` -> Displayed as `"OPEN"`.
    * **Benefit:** Debugging is no longer deciphering hex dumps; it is reading natural language.

### 4. Governance
The Map belongs to humanity.
* **License:** CC0 (Public Domain).
* **Management:** Managed by the Logos Foundation via open GitHub PRs.
* **Namespace:** Supports cultural diversity (e.g., `ID#China` maps to "China" and "中国").