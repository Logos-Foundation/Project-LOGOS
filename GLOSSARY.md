# Glossary (术语表)
## Project LOGOS Technical Vocabulary

> **"A shared vocabulary is the foundation of shared understanding."**

---

## Core Concepts (核心概念)

### Atom (原子)
A **64-bit value** representing a complete semantic unit. The fundamental data type of V.O.I.D. architecture.
- **Etymology**: Like physical atoms, Atoms are indivisible units that combine to form everything.
- **Contrast**: In OOP, an "object" is 128+ bits with headers and pointers. An Atom is exactly 64 bits.

### V.O.I.D. (虚空架构)
**Value Oriented Isomorphic Data** — The memory architecture of Project LOGOS.
- **Value Oriented**: Prefer stack-allocated values over heap-allocated objects.
- **Isomorphic**: Transformations preserve logical equivalence (lossless).
- **Data**: Everything is data; code is data too.

### Isomorphic Collapse (同构坍缩)
The **lossless transformation** from high-level object graphs to flat value streams.
- **Input**: `user.profile.settings.theme`
- **Output**: `LOAD [Base + Offset]`
- **Guarantee**: Semantics preserved, overhead eliminated.

---

## Atom Layouts (原子布局)

### Compact Atom (紧凑原子)
The **4-16-44** layout for 99% of use cases.
```
[TAG: 4-bit] [INDEX: 16-bit] [PAYLOAD: 44-bit]
```
- **Capacity**: 65,536 IDs, 7-char payload.

### Wide Atom (宽原子)
The **4-40-20** layout for large ID spaces.
```
[TAG: 4-bit] [EXTENDED_ID: 40-bit] [MINI-PAYLOAD: 20-bit]
```
- **Capacity**: 1 trillion IDs, 3-char payload.

### Pointer Atom (指针原子)
The **4-12-48** layout for heap objects.
```
[TAG: 4-bit] [META: 12-bit] [ADDRESS: 48-bit]
```
- **Use Case**: Large strings, blobs, legacy data.

---

## ID Topology (ID 拓扑)

### Ouroboros Ring (衔尾蛇环)
The **bidirectional ring buffer** for ID allocation.
- **Global Zone**: Grows from 0 → Max (Little-End).
- **Local Zone**: Grows from Max → 0 (Big-End).

### Möbius Ring (莫比乌斯环)
Evolution of Ouroboros emphasizing **topological unity**.
- Global and Local are the same surface, viewed from different angles.

---

## Encoding (编码)

### VSCP (Velo Standard Contraction Protocol)
The **abbreviation rules** for fitting strings into 44-bit payloads.
- **L1 Golden Intuition**: Pass through words ≤7 chars.
- **L2 Smart Numeronym**: `configuration` → `cfg9n`.
- **L3 Compound Skeleton**: `content-type` → `cnt-typ`.
- **L4 Vowel Drop**: `message` → `msg`.

### Velo-6
A **6-bit charset** `[a-z0-9_-]` enabling 7 characters in 44 bits.

### Velo-Han12
A **12-bit encoding** for CJK characters, enabling 3 chars + 8-bit meta.

---

## Hardware (硬件)

### SCP (Semantic Compute Processor)
The processor that **natively executes semantic atoms**.
- **Motto**: "Python is the native tongue."
- **Core Principle**: Match meaning, don't decode instructions.

### H-PU (Human Presentation Unit)
A **debugging co-processor** that translates IDs back to strings.
- Only active when a human attaches a debugger.
- Holds the Global Rosetta Map.

### Janus (双面神)
The **V1 hybrid architecture** with both legacy and SCP cores.

### SCP-Z (静默模式)
The **V2 native architecture** with zero payload (pure ID computing).

### Fractal (分形)
The **V3 8-bit architecture** for ultra-dense computing (IoT, bio-chips).

---

## Protocol (协议)

### Rosetta Map (罗塞塔映射图)
The **global ID-to-String mapping** for human civilization.
- **65,536 IDs** cover 99.9% of programming concepts.
- **CC0 Licensed**: Public domain, owned by humanity.

### WCI (Weighted Civilization Index)
The **allocation algorithm** for Rosetta IDs.
- **Criticality** ($C_w$): How fundamental is this concept?
- **GDP** ($E_w$): Economic importance.
- **Population** ($P_w$): How many people use this?

### Tag (标签)
The **4-bit mode selector** determining Atom interpretation.
- `0x0`: VOID/NULL
- `0x1`: Global Standard
- `0x2`: Local Dynamic
- `0xF`: Raw Pointer

---

## Philosophy (哲学)

### Negentropy (负熵)
**Reducing disorder** in computing by eliminating translation overhead.
- Opposite of entropy (chaos, waste).
- Goal: Minimum bits for maximum meaning.

### Type-II Civilization (二级文明)
A **stellar civilization** capable of harnessing the energy of its star.
- LOGOS aims to achieve Type-II through extreme efficiency, not brute force.

### Principle of Least Action (最小作用量原理)
Physics concept: **Nature takes the shortest path**.
- LOGOS: Computing should take the shortest path from intent to execution.

---

## See Also

- [Core Principles](./docs/philosophy/core_principles.md)
- [Design Decisions](./docs/philosophy/design_decisions.md)
- [RFC-0001: V.O.I.D. Architecture](./rfcs/0001-void-architecture.md)
- [RFC-0002: Rosetta Map](./rfcs/0002-rosetta-map.md)
- [RFC-0003: SCP Hardware](./rfcs/0003-scp-hardware.md)
