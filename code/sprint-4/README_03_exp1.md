For each experiment, use a sheet of paper (or your README) and work through these four steps:

```python
qc1 = QuantumCircuit(2, 2)

# apply X gate
qc1.x(0)

# Measure it
qc1.measure(0, 0)
qc1.measure(1, 1) 
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

q_0 --[0]---[X: flip]---[1]
q_1 --[0]----------------|------[0]
                         |       |
_________________________|_______|__
                        c_0     c_1
```

```bash
Read the classical register

c_0 = 1
c_1 = 0

Qiskit display order: highest classical-bit index first
'01'
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
       1   0 

Results
-------
{'01': 8901}

01: 100.0%
```