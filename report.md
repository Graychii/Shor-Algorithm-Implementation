# Report: Experimenting with Shor's Algorithm to Break RSA

## **Experiment Overview**

This report details the work conducted to test whether quantum computers can break RSA encryption by factoring RSA keys using Shor's algorithm. The experiment explored implementing Shor's algorithm with **Qiskit** and **Pennylane**, testing on both local simulators and IBM quantum hardware, to verify whether quantum computing can offer a significant advantage over classical methods for factoring RSA keys.

---

## **Introduction to Shor’s Algorithm**

Shor's algorithm is a quantum algorithm developed to factor large integers efficiently, offering a polynomial time solution compared to the exponential time complexity of classical algorithms. RSA encryption depends on the difficulty of factoring large composite numbers, which quantum algorithms, such as Shor's algorithm, can solve much more efficiently.

### **Key Components of Shor's Algorithm**:
1. **Quantum Fourier Transform (QFT)**: Helps in determining periodicity, essential for factoring large numbers.
2. **Modular Exponentiation**: A crucial step in calculating powers modulo a number.
3. **Continued Fraction Expansion**: Used to extract the period from the Quantum Fourier Transform.

---

## **Motivation**

The motivation behind this experiment was to explore whether quantum computers could efficiently break RSA encryption, a widely used cryptographic system based on the difficulty of factoring large composite numbers. RSA's security can be compromised if an algorithm, such as Shor's algorithm, can break the encryption by factoring its modulus.

---

## **Methodology**

### **Shor’s Algorithm Implementation**
The algorithm was implemented and tested using **Qiskit** (IBM’s quantum computing framework) and **Pennylane** (a quantum machine learning library). The goal was to test the feasibility of using quantum computers to factor RSA moduli, starting with small numbers like 15 and gradually progressing to larger moduli (up to 24 bits).

#### **Steps Taken**:
1. **Simulating Shor’s Algorithm**: Shor’s algorithm was first implemented and tested on local simulators with small RSA moduli (like 15) to simulate the factoring process.
2. **Connecting to IBM Quantum Hardware**: The IBM Quantum Experience API token was used to connect to IBM’s quantum hardware for real-time testing of Shor's algorithm.
3. **Testing Larger RSA Moduli**: The algorithm was tested on increasingly larger RSA moduli, with the first successful results observed on 24-bit RSA keys.

---

## **Key Findings**

### **Classical vs. Quantum Performance**
- **For small RSA modulu**, classical computers performed faster than quantum computers.
- **For 24-bit RSA modulu**, classical computers required over 4 minutes to break the key, while quantum computers completed the task in 8 seconds using Shor’s algorithm on IBM’s quantum hardware.

### **Testing Results**:
- **Local Simulations**: Shor's algorithm worked successfully on small numbers like moduli of 15, simulating the factorization process.
- **Quantum Hardware Testing**: On IBM's quantum system, the algorithm worked for RSA keys up to 24 bits. Beyond this, the hardware limitations became evident.
  
---

## **Hardware Limitations**
- IBM’s quantum hardware could only handle RSA moduli up to **24 bits** due to the **127 qubit limit** of the available system.
- Each quantum test was limited to a **10-minute window per month**, restricting the available testing time.
- **Quantum error correction** was not applied, which affected the reliability of the results in some cases.

### **Quantum vs. Classical Time Comparison**:

| **RSA Modulus Size** | **Classical Computing Time** | **Quantum Computing Time (IBM Quantum)** |
|----------------------|------------------------------|-------------------------------------------|
| 2-digit RSA          | < 1 second                   | 2–5 seconds                              |
| 24-bit RSA           | > 4 minutes                  | 8 seconds                                |

- **Classical Performance**: For small RSA moduli (up to 2 digits), classical computers easily outperformed quantum systems.
- **Quantum Performance**: For larger RSA moduli (24 bits), quantum systems showed a clear advantage, breaking the RSA encryption in **8 seconds** compared to **4 minutes** on classical computers.

- **Note**: For large numbers, the Brute Force approach proved to be the fastest, completing in ~2 seconds in classical computing. 

---

## **Challenges and Limitations**

1. **Quantum Hardware Accessibility**:
   - The limited number of qubits on IBM’s quantum hardware constrained the size of RSA keys that could be tested (up to 24 bits).
   - Availability of IBM's quantum hardware was restricted, with only **10 minutes of testing time** available per month, limiting the scope of the experiment.

2. **Classical Time Delays**:
   - Classical computers took a significantly longer time to break RSA keys as the modulus size increased, especially beyond 2 digits. However, for RSA moduli up to **24 bits**, the classical methods took more than **4 minutes**, while quantum computers took only **8 seconds**.

3. **Error Correction**:
   - Quantum error correction was not applied during the experiment, leading to occasional inconsistencies in the results. This is an area that can be improved for more reliable quantum computations in the future.

---

## **Conclusion and Future Work**

### **Conclusion**
The experiment demonstrated that Shor’s algorithm has the potential to break RSA encryption more efficiently than classical computers, especially when factoring larger RSA moduli (like 24 bits). However, the current limitations of quantum hardware—such as the number of qubits and the lack of error correction—restrict its ability to handle larger RSA moduli.

### **Future Directions**
1. **Hybrid Approaches**: Combining classical and quantum computing could offer a practical solution to factor larger RSA keys.
2. **Quantum Error Correction**: Implementing error correction techniques to enhance the reliability and accuracy of quantum computations is crucial for scaling the solution to larger numbers.

---

## **Requirements**

- **Python 3.x**
- **Qiskit**: IBM’s quantum computing framework.
- **Pennylane**: A quantum machine learning library for quantum circuits and simulations.
- **IBM Quantum Experience API Token**: Required to access IBM’s quantum hardware for real-time experiments.

