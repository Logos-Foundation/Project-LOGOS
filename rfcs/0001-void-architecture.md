# RFC-0001: V.O.I.D. Kernel Architecture
## V.O.I.D. 内核架构

| Metadata | Value |
| :--- | :--- |
| **RFC ID** | 0001 |
| **Title** | V.O.I.D. Architecture & Neutron Encoding Standard |
| **Version** | **0.9.0 (Draft)** |
| **Status** | **Active (Core Architecture)** |
| **Authors** | Velo Core Team (Human Architect & AI Copilot) |
| **Date** | 2026-01-11 |
| **Scope** | Memory Model, Atom Layout, ID Allocation, Encoding Protocol |

---

## 1. Core Definitions (核心定义)

Velo Runtime is based on the **V.O.I.D. (Value Oriented Isomorphic Data)** Architecture.
All data units are represented in registers as a **64-bit Atom**.

### 1.1 The Non-Zero Axiom (非零公理)
**Tag 0x0 (0000) MUST be reserved for NULL/VOID.**
*   Physical memory of `0x0000000000000000` represents "Nothingness".
*   **Engineering Benefit**: Allows Rust's `Option<Atom>` to use **Niche Optimization**, keeping the size at exactly 64-bit (no extra boolean flag).

---

## 2. Atom Layout Standards (原子位布局标准)

The **High 4 bits (Tag)** determine the polymorphic layout of the remaining 60 bits.

### 2.1 Compact Atom (The 4-16-44 Standard)
**Target**: Global IDs (< 65k) and Local IDs (< 65k offset). Covers 99% of use cases.

```plaintext
63      60 59              44 43                                          0
+--------+------------------+---------------------------------------------+
|  TAG   |      INDEX       |                   PAYLOAD                   |
| (4-bit)|     (16-bit)     |         (44-bit, 7 chars / 3.5 CJK)         |
+--------+------------------+---------------------------------------------+
```
*   **TAG (4-bit)**: Identity & Spacetime coordinate.
*   **INDEX (16-bit)**: Ring Buffer Offset.
*   **PAYLOAD (44-bit)**: Full Semantic Snapshot (7-char ASCII or 3-char CJK + Meta).

### 2.2 Wide Atom (The 4-40-20 Extended)
**Target**: Local ID Overflow (> 65k) or Future Library Expansion.

```plaintext
63      60 59                                      20 19                  0
+--------+-------------------------------------------+--------------------+
|  TAG   |               EXTENDED ID                 |    MINI-PAYLOAD    |
| (4-bit)|                (40-bit)                   |      (20-bit)      |
+--------+-------------------------------------------+--------------------+
```
*   **EXTENDED ID (40-bit)**: Capacity for **1 Trillion** objects.
*   **MINI-PAYLOAD (20-bit)**: Reserved for Micro-Hash or short tags. **Expansion Space.**
    *   *Usage*: Store 3-char abbreviation (`var`, `cfg`) or CRC20 checksum for collision detection.

### 2.3 Pointer Atom (The 4-12-48 Virtual)
**Target**: Large Objects, Blobs, Long Strings. Based on JVM Compressed Oops & x64 Canonical Address.

```plaintext
63      60 59        48 47                                                0
+--------+------------+---------------------------------------------------+
|  TAG   |    META    |                VIRTUAL ADDRESS                    |
| (4-bit)|  (12-bit)  |            (48-bit Canonical Pointers)            |
+--------+------------+---------------------------------------------------+
```
*   **TAG**: `0xF` (1111).
*   **VIRTUAL ADDRESS (48-bit)**: Matches Modern CPU (x86-64 Level 4 Paging) limit (256 TB).
    *   *Implementation*: `ptr = atom & 0x0000FFFFFFFFFFFF`.
*   **META (12-bit)**: **Micro-Metadata Space**.
    *   *Usage*: Store "GC Color", "Type Marker", or "Short Length" (< 4096).
    *   *Benefit*: Check string length without dereferencing pointer.

---

## 3. The Tag Spectrum (Tag 频谱)

The 4-bit Tag creates 16 parallel dimensions. "0 is Reserved".

| Binary | Hex | Name | Semantic Definition | Index Meaning | Payload Meaning |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0000** | **0x0** | **VOID / NULL** | **The Void**. Uninitialized Memory. | N/A | N/A |
| **0001** | **0x1** | **Global Std** | Standard Static Atom (Little-End) | Real ID = Index | Standard Alias (`config`) |
| **0010** | **0x2** | **Local Dyn** | Process Dynamic Atom (Big-End) | Real ID = `!Index` | Hash Fingerprint (`var~F1`) |
| **0011** | **0x3** | **Inline Str** | Tiny String (No Index) | N/A | 7-byte Raw ASCII |
| **0100** | **0x4** | **Inline Int** | Small Integer | N/A | 44-bit Signed Integer |
| `...` | `...` | *Reserved* | Future Expansion (Vector, Tensor) | ... | ... |
| **1111** | **0xF** | **Raw Pointer** | Heap Pointer (Layout Change) | Meta (12-bit) | Virtual Address (48-bit) |

---

## 4. ID Topology: The Ouroboros Ring (ID 拓扑)

The `u64` address space is a Bidirectional Ring Buffer.

1.  **Global Zone (Little-End)**:
    *   **Start**: 0 (Tag `0x1`)
    *   **Direction**: `0 -> 1 -> 2 ...`
    *   **Compute**: `RealID = Index`

2.  **Local Zone (Big-End)**:
    *   **Start**: Max (Tag `0x2`)
    *   **Direction**: `Max -> Max-1 ...`
    *   **Compute**: `RealID = !Index` (Bitwise NOT)

**The Adaptation Machine (自动降级)**:
*   **Compact**: Distance < 65,536 -> Use **4-16-44**.
*   **Wide**: Distance >= 65,536 -> Use **4-40-20**.
*   **Safety**: Guaranteed infinite capacity with graceful performance degradation (O(1) -> Table Lookup).

---

## 5. Encoding Protocol: VSCP (Velo Standard Contraction Protocol)

To maximize the **44-bit Payload**, we strictly enforce Velo Shorthand strategies.

### 5.1 English (Velo-6)
*   **Capacity**: 7 chars ($44 // 6 = 7$).
*   **Strategy Pipeline** (Priority: L0 > L1 > L2 > L3):
    1.  **L0 - Golden Intuition**: Direct pass-through for words ≤7 chars.
        *   `request` → `request` (7 chars, perfect fit)
        *   `config` → `config` (6 chars, perfect fit)
    2.  **L1 - Smart Numeronym**: Prefix(3) + Count + Suffix(1). (e.g., `transaction` -> `trx7n`)
    3.  **L2 - Compound Skeleton**: (e.g., `content-type` -> `cnt-typ`)
    4.  **L3 - Vowel Drop**: Strip non-leading vowels. (e.g., `message` -> `msg`)

### 5.2 Chinese (Velo-Han12)
*   **Capacity**: 3 chars + 8-bit Meta ($44 // 12 = 3.66$).
*   **Meta Usage**: Hash or Pinyin Initial to resolve collisions.
*   **Example**: `已发货` -> `[已][发][货][0x00]`.

---

## 6. Implementation Roadmap

### Phase 1: The Core
*   [ ] Define `struct Atom(u64)` in Rust.
*   [ ] Implement Tag enum and bitmask macros.
*   [ ] Verify `Option<Atom>` size is 64-bit (NonZero optimization).

### Phase 2: The Encoder
*   [ ] Implement VSCP algorithms (Velo-6 / Velo-Han12).
*   [ ] Generate `vstd.bin` (Global Rosetta Table) from Top 1000 Python libs.

### Phase 3: The Runtime
*   [ ] Implement Pointer Atom logic (48-bit masking).
*   [ ] Implement **Compact -> Wide** transition logic.

---

## 7. Optional Optimization: Heap Base Mode

**Target**: Memory-constrained environments with pre-allocated Velo Heap (4GB-32GB).

*   **Pointer Layout Change**:
    *   Store **32-bit Offset** instead of 48-bit Address.
    *   **Bonus**: 28-bit remain for inline metadata.
*   **Metadata Usage**:
    *   `len(str)` → O(1) register read (up to 256MB strings).
    *   `hash(str)` → Inline CRC/FNV snippet.
*   **Benefit**: String length and hash become **zero-dereference** operations.

---

> **Architect's Note**:
> This RFC incorporates **x64 architecture optimization** (48-bit addressing) and **JVM-level compression wisdom**.
> We have defined a system with **Micro-Excellence** (Compact Atom) and **Macro-Infinity** (Wide/Pointer Atom).