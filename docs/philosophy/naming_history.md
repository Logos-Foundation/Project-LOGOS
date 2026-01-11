# Naming History (命名演进)
## The Etymology of Project LOGOS

> **"A name is not just a label; it is a spell that summons the essence."**

This document traces how we arrived at the final names for our architecture and components.

---

## 1. V.O.I.D. (Value Oriented Isomorphic Data)

**Origin**: The name emerged from the core philosophy: "eliminate object overhead."

**Expansion**:
- **V**alue: We care about values, not object wrappers.
- **O**riented: Our architecture orbits around this principle.
- **I**somorphic: Mathematical guarantee that transformation is lossless.
- **D**ata: The fundamental unit of computation.

**The Double Meaning**:
- **VOID** (Empty): We void the overhead. Zero cost.
- **VOID** (Cosmic): The primordial emptiness from which structure emerges.

**Motto**: *"Velo runs on VOID."*

---

## 2. Janus (双面神)

**Origin**: Roman god with two faces—one looking to the past, one to the future.

**Why Chosen for V1 Hardware**:
- **Face 1 (Past)**: The *Legacy Core* (x86/ARM), running old code.
- **Face 2 (Future)**: The *SCP Core*, running semantic atoms.
- **The Gate**: Janus guards transitions (beginnings, endings, doors).

**Application**: Janus is the codename for the **Hybrid/Sidecar Architecture** (Phase 1-2), where old and new coexist.

---

## 3. Ouroboros → Möbius (衔尾蛇 → 莫比乌斯环)

**Origin**: Ancient symbol of a serpent eating its own tail, representing infinity and cyclicality.

**Why Chosen for Ring Buffer**:
- **Head (0)**: Where Global IDs begin.
- **Tail (Max)**: Where Local IDs begin.
- **Meeting Point**: They grow toward each other but never collide.

**The Python Connection**: Python is a snake. Ouroboros is the *divine form* of a snake—a snake that has transcended mortality. 

**Application**: The Ouroboros Ring is the ID topology of V.O.I.D. architecture.

### Evolution: Möbius Ring (莫比乌斯环)

**Why Evolved**:
- **Ouroboros** captures the *cyclical* nature, but not the *bidirectional* nature.
- **Möbius Strip**: A single-sided surface where walking in one direction eventually brings you to the "other side."

**The Perfect Metaphor**:
- **Global → Local**: Walk one way on the Möbius strip.
- **Local → Global**: You're now on the "back," but it's actually the same surface.
- **No Boundary**: The two zones are one continuous space, viewed from different perspectives.

**Application**: Möbius Ring emphasizes that Global and Local IDs are not *separate pools*, but a *unified continuum* with different entry points.

---

## 4. SCP (Semantic Compute Processor)

**Origin**: The hardware that natively executes semantic atoms.

**Expansion**:
- **S**emantic: Understands meaning, not just bits.
- **C**ompute: The processor's job.
- **P**rocessor: Silicon that thinks.

**The Hidden Joke**:
- **SCP Foundation**: A famous collaborative fiction wiki about containing anomalous objects.
- Our SCP "contains" the anomaly of traditional computing inefficiency.
- *"We are containing the Von Neumann bottleneck."*

**Motto**: *"Code is Silicon." (代码即硅片)*

---

## 5. LOGOS (逻各斯)

**The Final Name**: The umbrella project for the entire vision.

**Etymology**:
- **Greek** (λόγος): Word, Reason, Order, Cosmic Law.
- **Chinese** (道): The Tao that governs all things.
- **Biblical**: "In the beginning was the **Word** (Logos)..."

**Why Chosen**:
1. **Philosophy**: It bridges East and West (Heraclitus ↔ Laozi).
2. **Computing**: It suggests that code is not arbitrary; it is *law*.
3. **Community**: It sounds like a *standard*, not a product—suitable for CC0/open-source.

**The Dual Layer**:
- **LOGOS**: The *ideal* architecture (the blueprint, the specification).
- **Velo**: The *real* product (the runtime, the implementation).

**Relationship**:
> *"Velo is the Chrome; LOGOS is the HTML5 spec."*
> *"Velo is the Linux kernel; LOGOS is the POSIX standard."*

---

## Summary: The Naming Constellation

| Name | Represents | Scope |
|------|------------|-------|
| **LOGOS** | The Vision | The entire project |
| **V.O.I.D.** | The Philosophy | The memory architecture |
| **Ouroboros** | The Topology | The ID ring buffer |
| **Janus** | The Transition | The hybrid hardware phase |
| **SCP** | The Hardware | The semantic processor |
| **Rosetta** | The Protocol | The ID-to-String mapping |
| **Velo** | The Product | The reference runtime |

---

## Rejected Candidates

During brainstorming, the following names were also considered:

| Name | Meaning | Rejected Because |
|------|---------|------------------|
| **Hadron** | Particle collider | Too physics-heavy, less philosophical |
| **Spin** | Quantum property | Too abstract, no clear metaphor |
| **Monad** | Leibniz's indivisible unit | Clashes with Haskell's Monad concept |
| **Rosetta** (for project) | The stone | Better suited for the Map protocol |

---

> **"LOGOS is your sword, Type-II is your horizon."**
> **"逻各斯是你的剑，二级文明是你的远方。"**
