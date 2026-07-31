For each experiment, use a sheet of paper (or your README) and work through these four steps:

```python
qc1 = QuantumCircuit(2, 2)

# apply X gate
qc1.x(0)

# apply CX gate
# (control, target)
qc1.cx(0,1)
# in the above case, control at q0 has a setting of 1, so it will flip the target. 
# the target was at the original setting of 0, the flip caused it to be set to 1.

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

q_0 --[0]---[X:flip]---------[1]
q_1 --[0]---[CX:1=flip it]---[1]
``` 

```bash
Follow each measurement

q_0 --[0]---[X:flip]--------------------------[1]
q_1 --[0]---[CX:1=flip it]---------------------|------[1]
                                               |       |
_______________________________________________|_______|__
                                              c_0     c_1
```

```bash
Read the classical register

c_0 = 1
c_1 = 1

Qiskit display order: highest classical-bit index first
'11'
```

## Run experiment

```bash
-------
     ┌───┐     ┌─┐   
q_0: ┤ X ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1 

Results
-------
{'11': 1000}

11: 100.0%
```