"""
Objective

Learn that each qubit can be manipulated independently.

This is an important distinction because later you'll see gates that 
couple qubits together (such as CX). For now, we're proving that 
applying an X gate to one qubit has no effect on the other.
------------------------------------------------------------
Concept

With two qubits, there are four possible computational basis states:

State	Description
|00⟩	both qubits are 0
|01⟩	one qubit is 0, the other is 1
|10⟩	one qubit is 1, the other is 0
|11⟩	both qubits are 1
"""

from sys import argv

from helper_class import QuantumExperimentHandler
from qiskit import QuantumCircuit

LESSON_TITLE = "02 - Independent X Gates"

qeh = QuantumExperimentHandler()

# ---------------------------------------------------
"""
Experiment #1
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
Experiment #2
"""

qc2 = QuantumCircuit(2, 2)

# apply X gate
qc2.x(1)

# Measure it
qc2.measure(0, 0)
qc2.measure(1, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh = QuantumExperimentHandler()
qeh.run_experiment(name=f"{LESSON_TITLE} Exp 2", circuit=qc2, shots=shots)
#--------------------------------------------------
"""
Experiment #3
"""

qc3 = QuantumCircuit(2, 2)

# apply X gate
qc3.x(0)
qc3.x(1)

# Measure it
qc3.measure(0, 0)
qc3.measure(1, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh = QuantumExperimentHandler()
qeh.run_experiment(name=f"{LESSON_TITLE} Exp 3", circuit=qc3, shots=shots)

"""
Observation

Result interpretation
Experiment  Gates	        Qubit values    	Displayed result
1           X(q_0)	        q_0 = 1, q_1 = 0	01
2	        X(q_1)	        q_0 = 0, q_1 = 1	10
3	        X(q_0), X(q_1)	q_0 = 1, q_1 = 1	11


Qiskit displays multi-bit measurement results in classical-register 
order from highest index to lowest index. For a two-bit register, 
the displayed string is c_1c_0, so flipping q_0 and measuring it 
into c_0 produces 01.
"""