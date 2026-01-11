# RFC-0001: Semantic Compute Architecture (SCA)
## 语义计算架构规范

| Metadata | Value |
| :--- | :--- |
| **RFC ID** | 0001 |
| **Title** | Semantic Compute Architecture (SCA) |
| **Status** | **Active (Genesis)** |
| **Authors** | Project LOGOS Foundation |
| **License** | CC0-1.0 (Public Domain) |

---

## 1. Abstract (摘要)

**English:**
This document defines the **V.O.I.D.** (Value Oriented Isomorphic Data) architecture, the physical law of Project LOGOS. It specifies the "Neutron Atom" layout (4-16-44) for 64-bit registers and the "Ouroboros Ring" memory topology. It also outlines the long-term vision for the **SCP** (Semantic Compute Processor) hardware, which aims to eliminate the Von Neumann bottleneck through Zero-Decode and Memory-as-Compute technologies.

**中文:**
本文档定义了 **V.O.I.D.** (面向值的同构数据架构)，这是 Project LOGOS 的物理定律。它规范了 64 位寄存器内的“中子原子”(Neutron Atom) 布局 (4-16-44) 以及“衔尾蛇环”(Ouroboros Ring) 内存拓扑。同时，本文描绘了 **SCP** (语义计算处理器) 的硬件愿景，旨在通过零译码 (Zero-Decode) 和存算一体 (Memory-as-Compute) 技术彻底消除冯·诺依曼瓶颈。

---

## 2. V.O.I.D. Specification (V.O.I.D. 规范)

**Full Name**: Value Oriented Isomorphic Data
**中文全称**: 面向值的同构数据架构

### 2.1 The Neutron Atom (基础粒子：中子原子)

**Concept**: A specific bit-layout for the 64-bit register, achieving quantum coexistence of "Type + Index + Snapshot".
**概念**: 64-bit 寄存器内的极致位布局，实现“类型+索引+快照”的量子共存。

#### Layout Standard (布局标准): `4-16-44`

| Bits | Segment | Description (EN) | Description (CN) |
| :--- | :--- | :--- | :--- |
| **[63:60]** | **TAG** (4-bit) | **Identity.** Supports 15 states (Global, Local, Pointer, etc.). `0x0` is permanently reserved (Null). | **身份位**。支持 15 种状态（Global/Local/Pointer 等），0x0 永久留空。 |
| **[59:44]** | **INDEX** (16-bit) | **Addressing.** Physical offset in the ring buffer. Supports 65,536 extreme-speed channels. | **寻址位**。环形缓冲区的物理偏移量，支持 65,536 个极速通道。 |
| **[43:0]**  | **PAYLOAD** (44-bit) | **Data.** Stores semantic snapshot. Enables O(1) table-free debugging. | **数据位**。存储语义快照，实现 O(1) 无查表调试。 |

### 2.2 The Ouroboros Ring (时空拓扑：衔尾蛇环)

**Concept**: Using the `u64` address space to build a head-to-tail ring buffer, implementing bidirectional mirror allocation.
**概念**: 利用 `u64` 空间构建首尾相接的环形缓冲区，实现双向镜像分配。

*   **Global Zone (Forward Sequence / 正序)**:
    *   **The Foundation of Civilization.** Stores standard protocols and high-frequency terms. Immutable.
    *   **文明的基石**。存储标准协议与高频词。永恒不变。
*   **Local Zone (Reverse Sequence / 倒序)**:
    *   **The Flux of Runtime.** Stores temporary variables. Process-level lifecycle.
    *   **运行时的流变**。存储临时变量。进程级生命周期。

**Symmetry Principle (对称性原理)**: `Global = ID` vs `Local = !ID`

---

## 3. The Hardware Vision: SCP (硬件愿景：SCP 处理器)

**Codename**: SCP (Semantic Compute Processor)
**代号**: SCP (语义计算处理器)

### 3.1 Eliminating the Von Neumann Bottleneck (消灭冯·诺依曼瓶颈)

*   **Zero-Decode (零译码)**:
    *   Hardware recognizes the **Atom Tag** directly. No complex instruction decoding pipeline required.
    *   硬件直接识别 Atom Tag，无需复杂的指令译码流水线。
*   **Memory-as-Compute (存算一体 PIM)**:
    *   Simple ID comparison logic sinks into the memory modules (PIM). Bandwidth consumption reduced by an order of magnitude.
    *   简单的 ID 比对逻辑下沉至内存条 (PIM)，带宽消耗降低一个数量级。

### 3.2 Grand Unification (算力大一统)

*   **Logic & Compute Fusion**: Control flow (CPU strength) and Data flow (GPU strength) unified as **ID Stream Processing** at the lowest level.
    *   **逻辑与计算的融合**：控制流（CPU 强项）与数据流（GPU 强项）在底层统一为 ID 流处理。
*   **Architectural Isomorphism**: Future chips differ only in core count (Serial vs Parallel), separated by no instruction set barrier.
    *   **架构同构**：未来的计算芯片仅存在核心数量的区别（Serial vs Parallel），不再有指令集的隔阂。

### 3.3 Compute-View Separation (算视分离)

*   **H-PU (Human Presentation Unit)**:
    *   Physically separates "IDs for Machine calculation" from "Semantics for Human viewing".
    *   将“给机器算的 ID”与“给人看的语义”物理分离。
*   **Silent Mode (静默模式)**:
    *   The compute core runs in pure silence. Semantics are restored by the H-PU only when necessary.
    *   计算核心进入静默模式，仅在必要时由 H-PU 还原语义。