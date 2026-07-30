"""
Objective

- A qubit and a classical bit are not the same thing
- Measurement copies the qubit's value into a chosen classical bit
- Changing the measurement mapping changes the reported bitstring
------------------------------------------------------------
Concept

Think of the circuit as having two separate registers.

[ Quantum Register ]
q0
q1

[ Classical Register ]
c0
c1

The measurement operation is simply saying:
"Store the result of this qubit into this classical bit."
"""

from sys import argv

from helper_class import QuantumExperimentHandler
from qiskit import QuantumCircuit

LESSON_TITLE = "03 - Measurement Mapping"

qeh = QuantumExperimentHandler()

#--------------------------------------------------
"""
Experiment 1
"""
qc1 = QuantumCircuit(2, 2)

# apply X gate
qc1.x(0)

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

# Measure it
qc2.measure(0, 1)
qc2.measure(1, 0)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 2", circuit=qc2, shots=shots)

#--------------------------------------------------
"""
Experiment 3
"""
qc3 = QuantumCircuit(2, 2)

# apply X gate
qc3.x(1)

# Measure it
qc3.measure(1, 0)
qc3.measure(0, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 3", circuit=qc3, shots=shots)

#--------------------------------------------------
"""
Experiment 4
"""
qc4 = QuantumCircuit(2, 2)

# apply X gate
qc4.x(1)
qc4.x(0)

# Measure it
qc4.measure(1, 0)
qc4.measure(0, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 4", circuit=qc4, shots=shots)

#--------------------------------------------------
"""
Experiment 5
"""
qc4 = QuantumCircuit(2, 2)

# apply X gate
qc4.x(1)
qc4.x(1)

# Measure it
qc4.measure(1, 0)
qc4.measure(0, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 5", circuit=qc4, shots=shots)

#--------------------------------------------------
"""
Experiment 6
"""
qc4 = QuantumCircuit(2, 2)

# apply X gate
qc4.x(0)
qc4.x(1)

# Measure it
qc4.measure(0, 1)
qc4.measure(0, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 6", circuit=qc4, shots=shots)

"""
Observation

"""