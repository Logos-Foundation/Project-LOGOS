# Design Decisions (设计决策)
## The Rationale Behind V.O.I.D. Architecture

> **"Every bit in the 64-bit Atom has been fought for."**

This document records the **"Why"** behind key technical decisions. For the specification itself, see [RFC-0001](../../rfcs/0001-void-architecture.md).

---

## 1. Why 4-16-44? (为什么是 4-16-44?)

**Decision**: The Compact Atom layout is `[TAG: 4-bit] [INDEX: 16-bit] [PAYLOAD: 44-bit]`.

**Alternatives Considered**:
| Layout | TAG | INDEX | PAYLOAD | Rejected Because |
|--------|-----|-------|---------|------------------|
| 3-16-45 | 3b | 16b | 45b | Only 8 Tag states; not enough for future expansion |
| 4-20-40 | 4b | 20b | 40b | 40-bit payload = only 6 chars; loses "7-char intuition" |
| **4-16-44** | 4b | 16b | 44b | ✅ **Chosen**: 16 Tags, 65k IDs, 7 readable chars |

**Rationale**:
- **44-bit Payload** = $44 \div 6 = 7.33$ characters in Velo-6 encoding.
- **7 characters** covers 95%+ of common identifiers: `config`, `request`, `content`, `message`.
- **16-bit INDEX** = 65,536 slots, sufficient for global standard library + local variables.
- **4-bit TAG** = 16 dimensions, allowing future vectors, tensors, specialized types.

---

## 2. Why Tag 0 is VOID? (为什么 Tag 0 是虚空?)

**Decision**: `Tag 0x0 (0000)` is permanently reserved for NULL/VOID.

**The Non-Zero Axiom**:
- Physical memory `0x0000000000000000` represents "Nothingness."
- This allows Rust's `Option<Atom>` to use **Niche Optimization**.
- `sizeof(Option<Atom>) == sizeof(Atom) == 8 bytes` — no extra boolean flag needed.

**Alternative (Rejected)**:
- Use Tag 0 for a common type (e.g., Inline Int).
- **Problem**: Loses the "all-zeros = invalid" invariant, complicating null checks.

---

## 3. Why Ouroboros Ring? (为什么是衔尾蛇环?)

**Decision**: ID space is a bidirectional Ring Buffer, not a partitioned space.

```
Global Zone (Little-End):  0 → 1 → 2 → ... → 65535
Local Zone (Big-End):      Max → Max-1 → ... → Max-65535
```

**Rationale**:
- **Symmetry**: Both ends are "prime real estate" (close to origin = small index = fast).
- **No Collision**: Global grows up, Local grows down; they never meet.
- **Graceful Degradation**: When either exceeds 65k, automatically upgrade to Wide Atom.

**Naming**: The Ouroboros (衔尾蛇) symbolizes the head (0) and tail (Max) meeting, forming an infinite loop.

---

## 4. Why Compact vs Wide? (为什么分 Compact 和 Wide?)

**Decision**: Two Atom layouts exist for graceful performance degradation.

| Mode | Trigger | Layout | Payload |
|------|---------|--------|---------|
| **Compact** | Index < 65536 | 4-16-44 | Full 7-char |
| **Wide** | Index ≥ 65536 | 4-40-20 | Mini 3-char |

**Rationale**:
- **99.99% of applications** never exceed 65k symbols.
- For those that do (e.g., giant codebases), we trade payload for capacity.
- **Safety Guarantee**: ID space is infinite (40-bit = 1 trillion objects).

---

## 5. Why Velo-6 Encoding? (为什么使用 Velo-6 编码?)

**Decision**: Use a custom 6-bit charset `[a-z0-9_-]` for Payload.

**Alternatives Considered**:
| Encoding | Bits | Chars in 44-bit | Rejected Because |
|----------|------|-----------------|------------------|
| ASCII | 7b | 6 chars | Too few for `content-type` |
| UTF-8 | 8-32b | 1-5 chars | Variable width = complex parsing |
| **Velo-6** | 6b | 7 chars | ✅ Fixed width, human readable |

**Charset Philosophy**:
- Lowercase only (`a-z`): Case-insensitive matching.
- Numerals (`0-9`): Version numbers, IDs.
- Special (`_-`): Compound words like `content-type`.
- **No uppercase**: Saves 26 codes for future expansion.

---

## Summary: The Economy of Bits

Every decision above serves one goal: **Maximum meaning in minimum bits.**

| Resource | Allocation | Purpose |
|----------|------------|---------|
| 4 bits | TAG | Future-proofing (16 types) |
| 16 bits | INDEX | O(1) lookup for 99.99% cases |
| 44 bits | PAYLOAD | Human-readable debugging |

This is the **Principle of Least Action** applied to data representation.
