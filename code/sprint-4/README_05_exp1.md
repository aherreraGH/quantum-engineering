For each experiment, use a sheet of paper (or your README) and work through these four steps:

```python
qc1 = QuantumCircuit(2, 2)

# apply CX gate
# (control, target)
qc1.cx(0,1)

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

q_0 --[0]---[CX:0=no flip]---[1]
q_1 --[0]---[0]
``` 

```bash
Follow each measurement

q_0 --[0]---[CX:0=no flip]---[0]
q_1 --[0]---------------------|------[0]
                              |       |
______________________________|_______|__
                             c_0     c_1
```

```bash
Read the classical register

c_0 = 0
c_1 = 0

Qiskit display order: highest classical-bit index first
'00'
```

## Run experiment

```bash
-------
          ┌─┐   
q_0: ──■──┤M├───
     ┌─┴─┐└╥┘┌─┐
q_1: ┤ X ├─╫─┤M├
     └───┘ ║ └╥┘
c: 2/══════╩══╩═
           0  1 

Results
-------
{'00': 1000}

00: 100.0%
```