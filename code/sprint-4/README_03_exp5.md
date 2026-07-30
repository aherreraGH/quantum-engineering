For each experiment, use a sheet of paper (or your README) and work through these four steps:

```python
qc1 = QuantumCircuit(2, 2)

# apply X gate
qc4.x(1)
qc4.x(1)

# Measure it
qc4.measure(1, 0)
qc4.measure(0, 1)
```

```bash
Initial state

q_0 --[0]
q_1 --[0]
```

```bash
Apply each gate, one at a time

q_0 --[0]---[0]
q_1 --[0]---[X: flip]---[1]---[X: flip]---[0]
``` 

```bash
Follow each measurement

q_0 --[0]-----------------------------------------[0]
q_1 --[0]---[X: flip]---[1]---[X: flip]---[0]      |
                                           |       |
___________________________________________|_______|__
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
q_0: ─────┤M├────────
     ┌───┐└╥┘┌───┐┌─┐
q_1: ┤ X ├─╫─┤ X ├┤M├
     └───┘ ║ └───┘└╥┘
c: 2/══════╩═══════╩═
           1       0 

Results
-------
{'00': 1000}

00: 100.0%
```