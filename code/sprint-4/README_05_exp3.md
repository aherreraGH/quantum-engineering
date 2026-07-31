For each experiment, use a sheet of paper (or your README) and work through these four steps:

```python
qc3 = QuantumCircuit(2, 2)

# apply X gate
qc3.x(1)

# apply CX gate
qc3.cx(0,1)

# Measure it
qc3.measure(0, 0)
qc3.measure(1, 1)
```

```bash
Initial state

q_0 --[0]
q_1 --[0]
```

```bash
Apply each gate, one at a time

q_0 --[0]--------------------[0]
q_1 --[0]---[X:flip]---[1]---[CX:0=no flip]---[1]
``` 

```bash
Follow each measurement

q_0 --[0]-------------------------------------[0]
q_1 --[0]---[X:flip]---[1]---[CX:0=no flip]----|------[1]
                                               |       |
_______________________________________________|_______|__
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
               ┌─┐   
q_0: ───────■──┤M├───
     ┌───┐┌─┴─┐└╥┘┌─┐
q_1: ┤ X ├┤ X ├─╫─┤M├
     └───┘└───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1 

Results
-------
{'10': 1000}

10: 100.0%
```