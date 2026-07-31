"""
Objective

Learn how to create an entangled pair of qubits using only two gates:

Hadamard (H)
Controlled-X (CX)
"""

from sys import argv

from helper_class import QuantumExperimentHandler
from qiskit import QuantumCircuit

LESSON_TITLE = "05 - Creating Entanglement"

qeh = QuantumExperimentHandler()

#--------------------------------------------------
"""
Experiment 1
"""
qc1 = QuantumCircuit(2, 2)

# apply hadamard - creates 50/50
qc1.h(0)
# After hadamard is applied:
# q0 = superposition
# q1 = 0

# apply measures.
qc1.measure(0,0)
qc1.measure(1,1)
# q0 → c0
# q1 → c1

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 1", circuit=qc1, shots=shots)
#--------------------------------------------------
"""
Experiment 2
"""
qc2 = QuantumCircuit(2, 2)

# apply hadamard - creates 50/50
qc2.h(0)
# After hadamard is applied:
# q0 = superposition
# q1 = 0

# apply controlled-X
# control is q0, target is q1
qc2.cx(0,1)

# apply measures.
qc2.measure(0,0)
qc2.measure(1,1)


shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh.run_experiment(name=f"{LESSON_TITLE} Exp 2", circuit=qc2, shots=shots)
#--------------------------------------------------


"""
Observation

People often say:

"The qubits communicate."

Not really. A better way to think about it is:

The two qubits now describe one combined quantum state.

After entanglement, it no longer makes sense to completely describe either qubit by itself.
"""