from sys import argv

from helper_class import QuantumExperimentHandler
from qiskit import QuantumCircuit

LESSON_TITLE = "01 - Two Qubits"

qc = QuantumCircuit(2, 2)

# Measure it
qc.measure(0, 0)
qc.measure(1, 1)

shots = int(argv[1]) if len(argv) >= 2 else 1000

qeh = QuantumExperimentHandler()
qeh.run_experiment(name=LESSON_TITLE, circuit=qc, shots=shots)

"""
Observation

A two-qubit circuit initializes in the |00⟩ state. Without applying any gates, 
measuring both qubits always produces 00.
"""