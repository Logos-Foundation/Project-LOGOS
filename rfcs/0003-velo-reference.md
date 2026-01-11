# RFC-0003: Velo - The Reference Runtime

> **Status:** Active Product
> **Category:** Implementation

### 1. The Relationship: Logos & Velo
* **Logos** is the *Blueprint* (The Physics).
* **Velo** is the *Race Car* (The Product).

Velo is the immediate, pragmatic implementation of the Logos philosophy, designed to run on today's x86/ARM hardware.

### 2. Velo's Role
1.  **Proof of Concept:** Demonstrates that semantic compression (Atoms) yields 10x-50x performance gains even via software simulation.
2.  **Productization:** A drop-in replacement for Python runtimes, solving real-world latency issues now.
3.  **Bridge:** Velo serves as the "Ingest Module" for future SCP hardware. Code written for Velo today will be native to SCP chips tomorrow.

### 3. Technical Strategy
* **Memory Layout:** Velo adopts the Logos Atom specification for object storage.
* **Instruction Set:** Velo's bytecode is a software emulation of the SCP ISA.
* **Dual-Track Development:**
    * *Track A (Velo):* Focus on compatibility, ecosystem (PyPI), and JIT optimization.
    * *Track B (Logos):* Focus on hardware synthesis, FPGA verification, and standard definition.