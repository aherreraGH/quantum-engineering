# Sprint 4 — Two Qubits and Entanglement Foundations

## Objectives

- [ ] creating multi-qubit circuits
- [ ] addressing individual qubits
- [ ] measuring multiple qubits
- [ ] classical bit mapping
- [ ] independent qubits
- [ ] what entanglement is (conceptually)
- [ ] why a CX gate is special

## Questions Answered

| Lesson | Question Answered |
|--------|-------------------|
| 01 | why two qubits are different from one qubit |
| 02 | how to manipulate qubits independently |
| 03 | how classical bit mapping works |
| 04 | why two qubits in superposition produce four outcomes |
| 05 | what a controlled operation does |
| 06 | why a CX gate alone does not create entanglement |

## Pro Tips

### Python Engineering Tip #7

```text
When working with multiple qubits, start drawing the circuit on paper before you write code.

Even experienced quantum developers often sketch circuits first because it's much easier to reason about operations visually than by reading code alone. As circuits become more complex, that habit becomes increasingly valuable.
```

### Python Engineering Tip #8

```text
Start predicting every circuit before you execute it.

A good quantum engineer spends more time reasoning about the expected behavior than reading the simulator output. The simulator is there to verify your understanding—not to discover what the circuit does.
```

### Python Engineering Tip #9

```text
When debugging multi-qubit circuits, don't immediately assume a gate is wrong if the output looks reversed.

First verify:

- which qubit each gate operated on,
- which classical bit each qubit was measured into,
- and how the framework displays the classical register.

A large percentage of "my circuit is wrong" questions are actually measurement-mapping or bit-ordering misunderstandings.
```

## Quantum Computing Tips

The number of digits (or symbols) inside the ket tells you how many qubits are being described.

| State | Number of Qubits | Meaning |
|-------|------------------|---------|
| \|0⟩	| 1 | One qubit in state 0 |
| \|1⟩	| 1 | One qubit in state 1 |
| \|00⟩ | 2 | Two qubits, both in 0 |
| \|01⟩ | 2 | q0 and q1 have different values* |
| \|10⟩ | 2 | q0 and q1 have different values* |
| \|11⟩ | 2 | Two qubits, both in 1 |
| \|000⟩ | 3 | Three qubits, all in 0 |
