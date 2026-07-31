For each experiment, use a sheet of paper (or your README) and work through these four steps:

```python
qc1 = QuantumCircuit(2, 2)

# apply hadamard - creates 50/50
# combine states
qc1.h(0)

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

q_0 --[0]---[H]---{0|1}
q_1 --[0]
``` 

```bash
Follow each measurement

q_0 --[0]---[H]-------------{0|1}
q_1 --[0]---------------------|------[0]
                              |       |
______________________________|_______|__
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
01

Qiskit display order: highest classical-bit index first
{'00':<%value>,'01':<%value>}
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
{'00': 478, '11': 522}

00: 47.8%
11: 52.2%
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

----------------------------------
Mental model:
{0|1}

Formal notation:
(|0⟩ + |1⟩)/√2
"""