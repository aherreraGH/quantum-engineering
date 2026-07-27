from qiskit import QuantumCircuit

from helper_class import QuantumExperimentHandler

qh = QuantumExperimentHandler()

# Pauli
circuit = QuantumCircuit(1, 1)

circuit.x(0)
circuit.measure(0, 0)
print(circuit)

for shots in [1, 10, 100, 1000]:
    counts = qh.execute(circuit, shots)

    print(f"\nShots: {shots}")
    print(counts)

# Hadamard
circuit2 = QuantumCircuit(1, 1)

circuit2.h(0)
circuit2.measure(0, 0)
print(circuit2)

for shots in [1, 10, 100, 1000]:
    counts = qh.execute(circuit2, shots)

    print(f"\nShots: {shots}")
    print(counts)