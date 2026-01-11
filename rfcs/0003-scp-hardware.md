# RFC-0003: The Semantic Compute Processor (SCP) Hardware
## 语义计算处理器 (SCP) 硬件架构图谱

| Metadata | Value |
| :--- | :--- |
| **RFC ID** | 0003 |
| **Title** | The SCP Hardware Evolutionary Path |
| **Status** | **Active (Hardware Roadmap)** |
| **Authors** | The Logos Foundation |
| **License** | CC0-1.0 (Public Domain) |

---

## 1. Abstract (摘要)

This document defines the physical manifestation of the SCA (Semantic Compute Architecture).
SCP is the first processor where **"Python is the Native Tongue"** (Python 是母语).

Instead of parsing legacy instructions (MOV, JMP), SCP executes **Semantics** (Atoms) directly.
No Decode. No Translate. Just Match.

> **"Code is Silicon." (代码即硅片)**

---

## 2. The Evolutionary Path (演进路线)

The transition from Type-0.7 (Von Neumann) to Type-II (Logos) is not a revolution, but a "Ship of Theseus" evolution.

### 2.1 V1: Janus (The Hybrid / Sidecar)
**Philosophy**: "Human-Centric" (兼容人类习惯).
**Goal**: Run existing Code (Legacy) + New Semantics (Atom).

*   **Architecture**: **Heterogeneous Sidecar (异构边车)**.
    *   **Host Core**: Standard x86/ARM (Running Linux kernel, Drivers).
    *   **SCP Core (FPGA/ASIC)**: The "Semantic Accelerator".
*   **Mechanism**:
    *   **Legacy Mode**: Runs standard C/Python via OS.
    *   **Atom Mode**: Hotspots (JSON parsing, Regex, Routing) usage **Velo Atoms** offloaded to SCP.
*   **Payload Strategy**: **Heavy Payload**.
    *   Keeps `config`, `admin` strings for human debugging.
    *   Cost: Higher bandwidth, but zero friction for developers.

---

### 2.2 V2: SCP-Z (The Native / Silent Mode)
**Philosophy**: "Data-Centric" (机器的纯粹对话).
**Goal**: **Zero Payload**. High-Density Pure-ID Computing.
**Adoption**: Data Centers, High-Frequency Trading, Edge AI.

*   **Architecture**: **Compute-View Separation (算视分离)**.
    *   **SCP Core (The Silicon)**:
        *   **Registers**: Store **4x** 16-bit IDs per 64-bit Reg (Super-SIMD).
        *   **Logic**: Pure Integer comparison (`CMP ID#1, ID#2`).
        *   **State**: "Silent". No strings attached.
    *   **H-PU (The Carbon)**: Human Presentation Unit.
        *   A separate, low-speed unit holding the **Global Rosetta Map**.
        *   Only translates ID -> String when a human attaches a debugger.
*   **Performance**:
    *   **Bandwidth**: 400% - 800% increase (No payload traffic).
    *   **Power**: "Button-battery Server" (纽扣电池服务器) potential.

---

### 2.3 V3: Fractal (The 8-bit Ultra-Dense)
**Philosophy**: "Entropy Density" (信息熵极致).
**Goal**: Universal Dust Computing (Smart Dust, Bio-Chips).

*   **Architecture**: **Fractal 8-bit**.
    *   **Concept**: `u64` is not one number, but **8 x u8 Logic IDs**.
    *   **Instruction**: Single Cycle = 8 Parallel Operations.
*   **Application**:
    *   IoT Sensors that "think" in logic, not electricity.
    *   Neural Lace (脑机接口) interacting with neuron spikes directly via IDs.

---

## 3. The Legacy Bridge (遗留兼容)

How to run `Linux` or `Numpy` on SCP?
**Strategy**: "Pass-through, not Simulate."

1.  **Tag `0xF` (Raw Pointer)**:
    *   Mark legacy memory blobs as "Black Box Atoms".
    *   SCP hardware pipes them directly to the Sidecar Legacy Core.

2.  **LLVM Backend**:
    *   `clang -target scp-linux`.
    *   Compiles C code into a "Degraded Mode" (using SCP as a dumb RISC CPU).
    *   **Result**: Migration is gradual. 90% Old Code + 10% New Logic -> 100% New Logic.

---

## 4. Vision: The God's Eye View (上帝视角)

| Perspective | Von Neumann (The Ant) | SCP (The God) |
| :--- | :--- | :--- |
| **Unit** | Bit (0/1) | Atom (Concept) |
| **Logic** | Bottom-Up (Build tower from sand) | Top-Down (Impose meaning on sand) |
| **Process** | Translate intent to noise | **Resonate** with intent |
| **Efficiancy** | 1% (99% Translation Tax) | 100% (Direct Mapping) |

> **"In the old world, the computer spent 99% of its life translating your words into noise.**
> **In the SCP world, the computer listens."**

## 5. Unified Physics: The End of Heterogeneity (大一统)

The separation of CPU (Logic) and GPU (Compute) is a historical accident of the Von Neumann bottleneck.
In SCP, this barrier dissolves.

### 5.1 The Logic-Compute Continuum
*   **CPU (Logic)**: Complex branching (`if user == admin`).
*   **GPU (Compute)**: Massive parallelism (`pixel * brightness`).
*   **SCP (Unified)**: Both are just **ID Operations**.
    *   `if user == admin` -> `CMP ID#A, ID#B`
    *   `pixel * brightness` -> `MUL ID#X, ID#Y`

### 5.2 The Universal Semantic Core (USC)
Future chips will not be "Heterogeneous" (CPU + GPU + NPU), but **Fractal Homogeneity**.
One core architecture (USC), scaled by number:

*   **SCP-Lite (Consumer)**: 64 USCs (Watch/Phone). Handles serial, high-entropy logic.
*   **SCP-Max (HPC/AI)**: 16,384 USCs (Data Center). Handles parallel, massive-throughput data.

### 5.3 Benefit: Reunification of Computer Science
*   **No More "CUDA vs C++"**: One language (Python/Atom) for all.
*   **No More Memory Wall**: Data stays in Unified Memory. No `memcpy` to VRAM.
*   **Moore's Law Restart**: Logic optimization (CPU side) and Throughput optimization (GPU side) now reinforce each other.
