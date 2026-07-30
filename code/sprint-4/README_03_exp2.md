For each experiment, use a sheet of paper (or your README) and work through these four steps:

```python
qc1 = QuantumCircuit(2, 2)

# apply X gate
qc2.x(0)

# Measure it
qc2.measure(0, 1)
qc2.measure(1, 0)
```

```bash
Initial state

q_0 --[0]
q_1 --[0]
```

```bash
Apply each gate, one at a time

q_0 --[0]---[X: flip]---[1]
q_1 --[0]---[0]
``` 

```bash
Follow each measurement

q_0 --[0]---[X: flip]-----------[1]
q_1 --[0]---------------[0]      |
                         |       |
_________________________|_______|__
                        c_0     c_1
```

```bash
Read the classical register

c_0 = 0
c_1 = 1

Qiskit display order: highest classical-bit index first
'10'
```

## Run experiment

```bash
-------
     ┌───┐┌─┐
q_0: ┤ X ├┤M├
     └┬─┬┘└╥┘
q_1: ─┤M├──╫─
      └╥┘  ║ 
c: 2/══╩═══╩═
       0   1 

Results
-------
{'10': 8901}

10: 100.0%
```