# Experimenting with Shor's Algorithm to Break RSA

## Experiment Overview

The goal of this experiment was to implement Shor's algorithm and test its ability to break RSA encryption by factoring the RSA modulus. This work explores the practical challenges and considerations involved in leveraging quantum computing for cryptographic analysis.

## Introduction to Shor's Algorithm

Shor's algorithm is a quantum algorithm designed for factoring large integers efficiently. Unlike classical algorithms, which perform this task with exponential time complexity, Shor's algorithm utilizes quantum mechanics principles to achieve polynomial time complexity for this problem. Its efficiency is based on:

1. **Quantum Fourier Transform (QFT)**: To determine periodicity.
2. **Modular Exponentiation**: To compute powers modulo a number.
3. **Continued Fraction Expansion**: To extract the period from the QFT result.

## Motivation

This experiment was motivated by the potential application of Shor's algorithm to break RSA encryption, which relies on the difficulty of factoring large composite numbers. Testing Shor's algorithm on RSA-encrypted numbers provides insights into its practicality and limitations.

## Methodology

### 1. Implementation

- The algorithm was implemented using **Qiskit**, an open-source quantum computing framework that provides tools for building and simulating quantum circuits. The implementation focused on accurately constructing the quantum circuit for Shor's algorithm and performing modular exponentiation within the quantum framework.
  
- The implementation involved:
  
    - **Getting a Token**: Acquiring an IBM Quantum Experience API token to connect with IBM's RuntimeService for executing quantum circuits on actual quantum hardware.
  
    - **Connecting to RuntimeService**: Setting up the environment to access IBM's quantum resources and ensuring compatibility with the Qiskit runtime.
  
    - **Building the Circuit**: Constructing the quantum circuit for modular exponentiation and the Quantum Fourier Transform (QFT).
  
    - **Simulations**: Testing the algorithm on local simulators before deploying on IBM's quantum hardware.

### 2. Target

The RSA modulus, composed of two prime factors, was used as the target for factoring.

### 3. Base Selection

The base \( a \) for modular exponentiation was chosen randomly within the range. Key considerations included:

- The greatest common divisor (GCD) of \( a \) and \( N \) should ideally be 1.
- Behavior of the algorithm for specific base values.

## Key Steps in the Code:

1. **Loading IBMQ Account**:
    - The IBM Quantum Experience API token is used to load the account and get the provider for IBM quantum hardware.

2. **Running Shor’s Algorithm**:
    - The Shor object is used to factor a number \( N \) (in this case, the RSA modulus 15). The result shows the factors of \( N \).

## Limitations

### 1. Resource Availability

- IBM's quantum computing resources were not always accessible, causing delays in the experiment.

### 2. Lack of Documentation

- Comprehensive guidance for implementing Shor's algorithm in Pennylane is sparse, which led to additional challenges.
- Couldn’t connect to IBM properly, and since Qiskit was more compatible with IBM's service, we had to switch to it last minute.

### 3. Base Selection Challenges

- Some base choices did not match the expected behavior of the algorithm, leading to inefficiencies or failures in factoring.

### 4. Error Correction Considerations

- Quantum error correction was not incorporated, which impacted the reliability of the results.

## Results

- The experiment demonstrated the feasibility of implementing Shor's algorithm using Qiskit.
- Factoring smaller RSA-moduli was successful in some cases, though inconsistencies arose due to the limitations noted above.
