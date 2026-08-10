# 🛡️ UIDISA: Unified Intent-Driven Information Security Architecture

<p align="center">
  <img src="docs/assets/uidisa_banner.png" alt="UIDISA Banner" width="100%">
</p>

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Go 1.18+](https://img.shields.io/badge/Go-1.18+-00ADD8.svg)](https://golang.org/)
[![Build Status](https://img.shields.io/badge/Build-Passing-success.svg)](#)

An active, intent-driven cryptographic framework transitioning information security from **passive key-based protection** to **dynamic entropic data self-defense**.

---

## 📌 Table of Contents
- [Executive Summary](#-executive-summary)
- [Key Features & Innovations](#-key-features--innovations)
- [System Architecture & Workflow](#-system-architecture--workflow)
- [Complete Repository File Tree](#-complete-repository-file-tree)
- [Prerequisites](#-prerequisites)
- [Step-by-Step Installation & Execution Guide](#-step-by-step-installation--execution-guide)
  - [1. Running the Interactive CLI Dashboard](#1-running-the-interactive-cli-dashboard)
  - [2. Running the Core Pipeline Demo](#2-running-the-core-pipeline-demo)
  - [3. Running Automated Unit Tests](#3-running-automated-unit-tests)
  - [4. Executing High-Performance Go Native Engine](#4-executing-high-performance-go-native-engine)
- [Mathematical Formulation](#-mathematical-formulation)
- [Intellectual Property & Citation](#-intellectual-property--citation)

---

## 📖 Executive Summary

For over seven decades, global cybersecurity has relied on **passive encryption** (e.g., AES, TLS). Once intercepted, encrypted ciphertext remains static, leaving payloads vulnerable to offline cryptanalysis, supercomputing brute-force, and adversarial AI context injections.

**UIDISA** solves this fundamental vulnerability by embedding **Semantic Weight ($\Sigma$)** and a **Computational Intent Vector Matrix ($\vec{I}$)** directly into smart information units. 

If accessed outside of its authorized execution context or target environment, the payload permanently mutates into **irreversible mathematical noise** before decryption can ever be attempted.

---

## 🚀 Key Features & Innovations

* 🛡️ **Active Entropic Self-Defense ($\Delta \neq 0$):** Dynamic entropy barriers trigger immediate, non-recoverable payload corruption upon unauthorized access or environmental anomalies.
* 🧠 **Intent Verification Engine Matrix (IVEM):** Evaluates access requests using $\vec{I} = [\text{Goal} \times \text{Context} \times \text{Boundary}]^T$ to neutralize prompt injections and context-hijacking.
* 🧹 **Volatile RAM Sanitization:** Direct C-level memory zeroing and entropic overwriting routines prevent cold-boot and memory dump recovery attacks.
* ⚡ **Zero-Decryption Priority Routing:** Network infrastructure prioritizes high-value packets based on Semantic Weight ($\Sigma$) without needing payload decryption.
* 🏎️ **Dual-Engine Core Implementation:** Includes both Python Proof-of-Concept modules and ultra-low latency native Golang modules.

---

## 🏗️ System Architecture & Workflow

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      MODULE 1: SIU Engine                              │
 │   - Smart Information Unit Packager                                    │
 │   - Dynamic Entropy Calculator (Delta Barrier)                         │
 └───────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      MODULE 2: IVEM Audit Engine                       │
 │   - Real-time Goal x Context x Boundary Evaluator                      │
 │   - Environmental Hash & Anomaly Detector                              │
 └───────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │            MODULE 3: Entropic Self-Defense & RAM Wiper                 │
 │   - Irreversible Mathematical Noise Injector                           │
 │   - Non-recoverable Volatile Memory Erasure                            │
 └────────────────────────────────────────────────────────────────────────┘
```
📁 Complete Repository File Tree
```bash
UIDISA-Architecture/
├── README.md                 <-- Comprehensive System Overview & Usage Guide
├── WHITEPAPER.md             <-- Complete Academic Whitepaper
├── LICENSE                   <-- Creative Commons CC BY-NC-ND 4.0 License
├── CITATION.cff              <-- Academic Citation Metadata
├── .github/
│   └── workflows/
│       └── python-tests.yml  <-- CI/CD Automated Test Pipeline
├── tests/
│   ├── test_siu.py           <-- Unit Tests for SIU Packager
│   └── test_ivem.py          <-- Unit Tests for IVEM Audit Engine
└── uidisa_core/
    ├── main_demo.py          <-- Core Pipeline Verification Script
    ├── cli.py                <-- Interactive Live Workbench & Attack Simulator
    ├── siu/                  <-- Module 1: Smart Information Unit
    │   ├── crypto.py         <-- Math Scrambler & Noise Engine
    │   └── packet.py         <-- SIU Packet & Entropy Barrier
    ├── ivem/                 <-- Module 2: Intent Matrix Auditor
    │   ├── matrix.py         <-- Dynamic Intent Vector Logic
    │   └── audit.py          <-- Real-Time Audit Engine
    ├── defense/              <-- Module 3: Active Defense Mechanisms
    │   └── memory_wiper.py   <-- C-Level Volatile RAM Sanitizer
    └── go_core/              <-- Native High-Performance Module
        └── uidisa.go         <-- Low-Latency Golang Engine
```
## ⚙️ Prerequisites
Ensure you have the following installed on your system:
 * Python: 3.8 or higher
 * Go (Optional for Go Native Engine): 1.18 or higher
 * Git: Installed and configured
## 🛠️ Step-by-Step Installation & Execution Guide
Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone [https://github.com/mkfih3r/UIDISA-Architecture.git](https://github.com/mkfih3r/UIDISA-Architecture.git)
cd UIDISA-Architecture
```
## 1. Running the Interactive CLI Dashboard
Launch the live interactive workbench to package custom payloads, simulate real-time Man-In-The-Middle (MITM) attacks, and inspect volatile memory sanitization:
```bash
python uidisa_core/cli.py
```
# Interactive Menu Options:
 * i. Package Payload into SIU: Assign Semantic Weight (\Sigma) and environmental hashes to package raw data.
 * ii. Simulate Authorized Decryption: Observe clean payload extraction under validated intent conditions.
 * iii. Simulate MITM Attack / Context Hijack: Watch the system trigger entropic self-destruction when an unauthorized node attempts access.
 * iv. Inspect Volatile Memory State Wiper: Observe hardware-level byte overwriting in real time.
# 2. Running the Core Pipeline Demo
To run an automated execution flow demonstrating authorized access vs. malicious interception:
```bash
python uidisa_core/main_demo.py
```
# 3. Running Automated Unit Tests
Ensure all components are functioning securely using pytest:
# Install pytest (if not already installed)
```bash
pip install pytest
```
# Run all unit tests
```bash
pytest
```
4. Executing High-Performance Go Native Engine
To test the ultra-fast Go implementation designed for low-latency systems (e.g., V2X Automotive ECUs, IoT Gateways):
```bash
cd uidisa_core/go_core
go run uidisa.go
```
## 🧮 Mathematical Formulation
### 1. Smart Information Unit (SIU) Formulation
The Smart Information Unit (SIU) is defined as a 3-tuple state space that binds the scrambled payload tensor, semantic priority, and the active entropic barrier:

$$\text{SIU} = \langle P, \Sigma, \Delta \rangle$$

Where:
* **$P$ (Scrambled Payload Tensor):** Represented as
**$P = f_{\text{scramble}}(M, \mathbf{K}_{\text{context}})$,**
where $M$ is the plaintext payload and
**$\mathbf{K}_{\text{context}}$**
is the dynamic context key matrix derived from environmental entropy.
* **$\Sigma \in [0.0, 1.0]^{m \times n}$
(Semantic Weight Matrix):** A normalized matrix/tensor defining the relative utility and routing priority of the packet across zero-decryption network nodes.
* **$\Sigma \in [0.0, 1.0]^{m \times n}$ (Semantic Weight Matrix):** A normalized matrix/tensor defining the relative utility and routing priority of the packet across zero-decryption network nodes.
* **$\Delta \in \{0, 1\}$ (Dynamic Entropy Barrier):** A boolean indicator flag evaluated via a Hamming distance threshold against the execution context:

$$\Delta = \mathbb{I}\left( d_H\left(\mathcal{H}(\text{Env}_{\text{current}}), \mathcal{H}(\text{Env}_{\text{target}})\right) > \tau \right)$$

Where:
* $d_H(\mathbf{a}, \mathbf{b}) = \sum_{i=1}^{N} (a_i \oplus b_i)$ calculates the bit-level Hamming distance.
* $\tau$ is the maximum acceptable noise tolerance threshold.
* $\mathbb{I}(\cdot) = 1$ triggers active payload corruption.
---

### 2. Computational Intent Vector Matrix ($\vec{I}$)
The Intent Verification Engine Matrix (IVEM) evaluates the validity of an incoming access request using a multi-dimensional matrix cross-product:

$$\vec{I} = \begin{bmatrix} \mathbf{G} \\ \mathbf{C} \\ \mathbf{B} \end{bmatrix} = [\text{Goal} \times \text{Context} \times \text{Boundary}]^T$$

Where:
* **$\mathbf{G}$ (Goal Vector):** Evaluates system prompt integrity and operational objectives.
* **$\mathbf{C}$ (Context Vector):** Validates caller environment, execution state, and cryptographic nonces.
* **$\mathbf{B}$ (Boundary Vector):** Enforces hard computational, network, and access limitations.

---

system prompt integrity and operational objectives.
* **$\mathbf{C}$ (Context Vector):** Validates caller environment, execution state, and cryptographic nonces.
* **$\mathbf{B}$ (Boundary Vector):** Enforces hard computational, network, and access limitations.

---

### 3. Active Entropic Self-Defense Transformation
If access is requested outside the validated intent boundary or environmental noise exceeds the allowable threshold ($\Delta \neq 0$), the payload undergoes immediate and non-recoverable entropic corruption:

$$\text{If } \Delta \neq 0 \implies P \leftarrow P \oplus \mathcal{N}_{\text{entropy}}$$

Where $\mathcal{N}_{\text{entropy}}$ represents pseudo-random mathematical noise injected directly at the memory byte-level, causing irreversible payload degradation before decryption algorithms can process the data.
payload degradation before decryption algorithms can process the data.

## 📜 Intellectual Property & Citation
```text
Copyright © 2026 md kazi Fuadul islam. All Rights Reserved.
Distributed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license.
```
# Citing UIDISA
If you use, reference, or evaluate this security architecture in research or software implementation, please cite it using:
```
@misc{islam2026uidisa,
  author = {mkfih3r},
  title = {UIDISA: Unified Intent-Driven Information Security Architecture},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{[https://github.com/mkfih3r/UIDISA-Architecture](https://github.com/mkfih3r/UIDISA-Architecture)}}
}
```
