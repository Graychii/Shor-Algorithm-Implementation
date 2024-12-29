# Shor Algorithm Implementation  

This repository contains implementations of Shor's algorithm using quantum computing frameworks, with both generalized and simplified approaches. The project explores the quantum factorization of integers and provides implementations using **Qiskit** and **PennyLane**.  

## Overview  

Shor's algorithm is a quantum algorithm that efficiently factors integers. It demonstrates the power of quantum computing to solve problems that are infeasible for classical computers.  

This repository includes:  
- A **generalized implementation** of Shor's algorithm tested with **Qiskit** and **PennyLane**.  
- A **simplified implementation** tailored for factoring 15.  

The project serves as both a learning tool and a reference for quantum computing enthusiasts.  

---

## Repository Structure  

```plaintext  
├── generalization  
│   ├── pennylane  
│   │   └── shor_pennylane.ipynb     # Generalized implementation using PennyLane.  
│   ├── qiskit  
│   │   ├── denominator.py          # Helper functions for the Qiskit implementation.  
│   │   └── Shor.ipynb              # Generalized implementation using Qiskit.  
├── simplified  
│   └── shor.ipynb                  # Simplified version of Shor's algorithm (mod 15).  
├── README.md                       # This README file.  
├── report.md                       # Detailed project report and explanation.  
