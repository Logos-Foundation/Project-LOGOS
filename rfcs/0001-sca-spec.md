# RFC-0001: Semantic Compute Architecture (SCA)

> **Status:** Draft
> **Category:** Specification

### 1. The Core Definition
**SCA** is an architecture where the CPU processes **Semantic Atoms** instead of raw bytes.
It closes the "Semantic Gap" not by software virtualization, but by hardware realization.

### 2. The Atom Structure
An Atom is the fundamental unit of Logos.

* **The 64-bit View (Standard):**
    * `Tag (4-bit)`: Defines type (e.g., Global ID, Local Pointer, Raw Data).
    * `Payload (60-bit)`: The Unique Semantic ID (from the Rosetta Map).
* **The 8-bit View (Compact/Fractal):**
    * For edge devices or high-density throughput, we utilize information entropy.
    * Common ops (`True`, `Add`, `Load`) are compressed into 8-bit Nano-Atoms.
    * **"u64 = u512"**: A single 64-bit register can hold 8 parallel semantic instructions.

### 3. SCP: The Semantic Compute Processor
The hardware implementation of SCA.

* **No Decode Stage:** The ID *is* the instruction.
* **SCP-Z (Zero Payload):** The ultimate "Silent Mode." The core processes pure IDs. The "String" (Payload) is stripped away at the Ingest stage.
* **Execution:**
    * Legacy: `strcmp(a, b)` -> 500 cycles.
    * SCP: `CMP ID_A, ID_B` -> 1 cycle.

### 4. The Unified Semantic Core (USC)
SCA unifies the CPU and GPU.
* **CPU Logic:** Handling branching is just handling `ID#Jump`.
* **GPU Math:** Handling matrix multiplication is just handling stream of `ID#Float`.
* Difference is only in scale:
    * **SCP-Lite:** 64 Cores (Logic heavy).
    * **SCP-Max:** 16,384 Cores (Throughput heavy).
    * **End of Heterogeneous Hell:** Same compiler, same Atoms, different scale.

### 5. Legacy Compatibility (The Ship of Theseus)
We do not discard the past.
* **Sidecar / Raw Mode:** SCP supports a `Legacy Atom` (Tag `0xF`).
* **Behavior:** When `Tag=Raw`, the core behaves like a standard RISC processor, executing legacy C/Linux code.
* **Evolution:** We replace the OS layer by layer, from "Raw Bytes" to "Semantic Atoms," while the system keeps running.