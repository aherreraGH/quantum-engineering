For each experiment, use a sheet of paper (or your README) and work through these four steps:

```python
qc1 = QuantumCircuit(2, 2)

# apply hadamard - creates 50/50
# combine states
qc1.h(0)

# apply controlled-X
# control is q0, target is q1
qc1.cx(0,1)

# apply measures.
qc1.measure(0,0)
qc1.measure(1,1)
```

```bash
Initial state

q_0 --[0]
q_1 --[0]
```

```bash
Apply each gate, one at a time

q_0 --[0]---[H]-----{0|1}
q_1 --[0]---[CX:0]---[0]

# CX checks the control qubit.
# - If q0 measures as |0⟩, q1 stays 0.
# - If q0 measures as |1⟩, q1 flips to 1.
``` 

```bash
Follow each measurement

q_0 --[0]---[H]---{0|1}
q_1 --[0]-----------|------[0]
                    |       |
____________________|_______|__
                   c_0     c_1
```

```bash
Read the classical register

c1 c0
│  │
│  └── changes (0 or 1)
└──── always 0

Which produces:

00
11 # this happens because the cx call flips when |1 is shown

Qiskit display order: highest classical-bit index first
{'00':<%value>,'11':<%value>}
```

## Run experiment

```bash
-------
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1 

Results
-------
{'00': 499, '11': 501}

00: 49.9%
11: 50.1%
```

"""
Observation

What does the √2 do?

The 1/√2 is called the amplitude. Its job is to normalize the quantum state so the probabilities add up to 100%.

So:

(|0⟩ + |1⟩) / √2

means:

Amplitude of |0⟩ = 1/√2
Amplitude of |1⟩ = 1/√2

which becomes:

Probability of |0⟩ = 50%
Probability of |1⟩ = 50%
"""