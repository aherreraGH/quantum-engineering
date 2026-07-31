"""
Objective

- what a control qubit is
- what a target qubit is
- when a CX gate flips a qubit
- how to predict its behavior before executing a circuit
------------------------------------------------------------
Concept


Truth Table
------------------------------------
Control Target Before	Target After
0	    0	            0
0	    1	            1
1	    0	            1
1	    1	            0

Notice:

- first column determines everything
- second column only changes when control = 1
"""

from sys import argv

from helper_class import QuantumExperimentHandler
from qiskit import QuantumCircuit

LESSON_TITLE = "05 - CX Gate"

qeh = QuantumExperimentHandler()

#--------------------------------------------------
"""
Experiment 1
"""
qc1 = QuantumCircuit(2, 2)

# apply CX gate
qc1.cx(0,1)

# Measure it
qc1.measure(0, 0)
qc1.measure(1, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 1", circuit=qc1, shots=shots)
#--------------------------------------------------
"""
Experiment 2
"""
qc2 = QuantumCircuit(2, 2)

# apply X gate
qc2.x(0)

# apply CX gate
qc2.cx(0,1)

# Measure it
qc2.measure(0, 0)
qc2.measure(1, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 2", circuit=qc2, shots=shots)
#--------------------------------------------------
"""
Experiment 3
"""
qc3 = QuantumCircuit(2, 2)

# apply X gate
qc3.x(1)

# apply CX gate
qc3.cx(0,1)

# Measure it
qc3.measure(0, 0)
qc3.measure(1, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 3", circuit=qc3, shots=shots)
