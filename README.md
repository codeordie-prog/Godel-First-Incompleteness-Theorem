# Gödel's First Incompleteness Theorem

![Gödel](image/godel.png)

## Overview

This repository provides a toy implementation to illustrate Gödel's first incompleteness theorem using a simple formal system, a set of axioms, and Gödel numbering (coding).

### What is Gödel's First Incompleteness Theorem?
Gödel's first incompleteness theorem states that in any consistent, sufficiently expressive formal system, there exist true statements that cannot be proven within the system itself. In other words, no such system can be both complete (able to prove every truth) and consistent (never proving a falsehood).

### How This Repository Illustrates the Theorem
- **Toy Formal System**: The code defines a minimal formal system with a small set of axioms (see `axioms.py`).
- **Gödel Coding**: Statements and axioms are encoded as numbers using Gödel numbering (see `godel_code.py`).
- **Proof Engine**: The `Proof_Engine` (in `formal_system.py`) attempts to prove statements by applying inference rules to the axioms and checking if the statement can be derived.
- **Unprovable Statement**: The system includes a self-referential statement ("This statement is not provable") to demonstrate incompleteness. The proof engine cannot derive this statement from the axioms, illustrating the existence of true but unprovable statements within the system.

### Running the Example
Run `formalsystem/test.py` to see the proof engine in action. The output will show whether the system can prove the self-referential statement, highlighting the incompleteness phenomenon.

---

This project is for educational purposes and provides a simplified, illustrative version of Gödel's profound result.
