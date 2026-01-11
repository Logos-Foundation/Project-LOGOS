# RFC-0002: The Global Rosetta Map
## 全球罗塞塔映射图

| Metadata | Value |
| :--- | :--- |
| **RFC ID** | 0002 |
| **Title** | The Global Rosetta Map & Protocol |
| **Status** | **Active (Civilization Grade)** |
| **Authors** | The Logos Foundation |
| **License** | CC0-1.0 (Public Domain) |

---

## 1. Abstract (摘要)

The **Global Rosetta Map** is the "Civilization Base Encoding" for a Type-II Civilization. It acts as the universal bridge between Carbon-based language (Strings/Code) and Silicon-based reality (Atoms/IDs).

It unifies all human concepts—language, code, commerce, and industry—into a single, decentralized, **O(1) resolvable** semantic substrate.

---

## 2. Philosophy: Dictionary of Earth Civilization

The Map is not merely a software optimization; it is the **Universal Index of Earth Civilization**.
它不仅仅是软件的优化，它是**地球文明的通用索引**。

### 2.1 Semantic Co-existence (语义共存)
Unlike traditional translators that force "Unification" (mapping everything to English), Rosetta ensures **"Data Neutrality"**.
*   **English**: `Money` -> `ID #0x0501`
*   **Chinese**: `钱` -> `ID #0x0500`
*   **Principle**: **Semantic Independence, ID Isolation.**
    *   If a user writes in Chinese, Velo preserves it as a Chinese concept (ID #0x0500).
    *   If a user writes in English, Velo preserves it as an English concept (ID #0x0501).
    *   **Result**: No translation loss. The "Tower of Babel" is not destroyed; it is indexed perfectly.

---

## 3. The Protocol Specification (协议规范)

This section defines the rigorous technical rules for implementation. There is **NO** ambiguity.

### 3.1 The Value-Oriented Isomorphic Data (V.O.I.D.) Atom
Every 64-bit Atom in Velo follows this precise layout to enable "Semantic Holography".
**Synced with RFC-0001: The 4-16-44 Standard.**

| Bit Range | Length | Component | Description |
| :--- | :--- | :--- | :--- |
| **63 - 60** | 4 bits | **Tag** | The Mode Selector (16 Dimensions). `0000` is VOID. |
| **59 - 44** | 16 bits | **Index** | The Ring Buffer Offset (0 - 65,535). |
| **43 - 0** | 44 bits | **Payload** | The "Squeezed String" (44-bit data). |

### 3.2 The Tagging Strategy (Tag Spec)
The Tag determines the interpretation of the Payload.

*   **Tag `0000`: VOID / NULL**
    *   **Definition**: The semantic void. Uninitialized memory.
    *   **Effect**: Allows Rust `Option<Atom>` Niche Optimization.

*   **Tag `0001`: Global Std (Direct Mode)**
    *   **Definition**: The Standard Static Atom.
    *   **Use Case**: Short keywords (`if`, `len`) or Standard Aliases (`config`).
    *   **Resolution**: `print(payload)`. **Zero lookup.**

*   **Tag `0010`: Local Dyn (Local Mode)**
    *   **Definition**: Process-local dynamic variables.
    *   **Index Logic**: `RealID = !Index` (Bitwise Not).
    *   **Resolution**: `print(ROSETTA_EXPANSION[ID])`.

### 3.3 The Abbreviation Dialect (Velo Shorthand)
To compress Civilization Concepts into **44 bits (7 chars max)**, we strictly enforce the **Velo Shorthand Dialect**. Rules are prioritized L1 > L2 > L3.

#### L1: Golden Intuition (黄金直觉)
Direct 7-char pass-through. If word ≤7 chars, use as-is.
*   `request` → `request` (7 chars, fits)
*   `config` → `config` (6 chars, fits)
*   `admin` → `admin` (5 chars, fits)

#### L2: Smart Numeronym (智能数字缩写)
For words >7 chars: Prefix(3) + Middle Count + Suffix(1).
*   `transaction` → `trx7n` (3 + "7" + 1 = 5 chars)
*   `configuration` → `cfg9n` (3 + "9" + 1 = 5 chars)
*   `kubernetes` → `k8s` (whitelisted exception)

#### L3: Compound Skeleton (复合词骨架)
For hyphenated (`-`) or underscored (`_`) terms, take consonant skeletons of each part.
*   `content-length` → `cnt-len` (7 chars, fits!)
*   `content-type` → `cnt-typ` (7 chars, fits!)
*   `user-agent` → `usr-agt` (7 chars, fits!)

#### L4: Vowel Drop (元音剔除)
Strip non-leading vowels to retain the "Consonant Skeleton".
*   `message` → `msg`
*   `background` → `bg`

---

## 4. The Global Rosetta Table (Allocations)

The 65,536 IDs conform to the **Weighted Civilization Index (WCI)**.
This is the **Immutable Genesis Block** of the protocol.

| ID Range (Hex) | Tier Name | WCI Strategy | Examples (ID -> Alias -> Full) |
| :--- | :--- | :--- | :--- |
| **0x0000 - 0x0FFF** | **The Axioms (Tier 0)** | Criticality ($C_w$) | `0x0001` -> `true`<br>`0x0100` -> `len`<br>`0x0500` -> `钱` (CN Logic) |
| **0x1000 - 0x1FFF** | **Object Model** | Criticality ($C_w$) | `0x1001` -> `__init` -> `__init__`<br>`0x1002` -> `__str` -> `__str__` |
| **0x2000 - 0x4FFF** | **Web & Net (Tier 1)** | GDP ($E_w$) | `0x2056` -> `cnt-len` -> `content-length`<br>`0x2055` -> `cnt-typ` -> `content-type`<br>`0x2001` -> `GET` |
| **0x5000 - 0x6FFF** | **Biz & Logic (Tier 2)** | GDP ($E_w$) | `0x5001` -> `config` -> `config`<br>`0x5002` -> `configr` -> `configuration`<br>`0x0501` -> `Money` |
| **0x7000 - 0xFFFF** | **The Commons (Tier 3)** | Pop ($P_w$) | `0x7001` -> `user`<br>`0x7088` -> `用户` (CN Alias)<br>`0x7089` -> `ユーザー` (JP Alias) |

---

## 5. Technical Implementation Details (技术细节)

### 5.1 Velo-6 Encoding
To fit 7 characters into 44 bits, we use a custom 6-bit charset: `[a-z0-9_]`.
*   **Capacity**: $44 / 6 = 7.33$ characters (Safe for 7 chars).
*   **Illegal Chars**: Upper case (mapped to lower), special symbols (mapped to `_` or handled by ID).

### 5.2 The Resolution Algorithm
How to turn an ID back into a Human String (e.g., for JSON export):

```rust
fn resolve_atom(atom: u64) -> &str {
    let tag = (atom >> 60) & 0xF; // 4-bit Tag
    let index = (atom >> 44) & 0xFFFF; // 16-bit Index
    let payload = atom & 0xFFFFFFFFFFF; // 44-bit Payload

    match tag {
        0x1 => decode_velo6(payload), // Global Std: "GET"
        0x2 => resolve_local(index),  // Local Dyn: Consult Stack Table
        _   => "UNKNOWN"
    }
}
```

### 5.3 Conflict Resolution (The Law)
*   **Collision Proof**: If a user variable collides with a Tier 0-2 ID, it is forced to **Tag 0x2** (Local).
*   **Canonical Truth**: `ID #0x2056` is ALWAYS `content-length`. No local override is permitted.

---

## 6. Vision: The DNS of Meaning

By standardizing these 65,536 atoms, we achieve:
1.  **Zero-Overhead Communication**: Services exchange IDs, not JSON strings.
2.  **Universal Debugging**: `cnt-len` is readable by humans, `0x2056` is readable by chips.
3.  **Civilization Preservation**: The concepts of 21st-century humanity are etched into the silicon index.

> **"Code is Physics. Logic is Law."**