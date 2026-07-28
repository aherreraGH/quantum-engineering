from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from sys import argv
from qiskit import QuantumRegister, ClassicalRegister

qc = QuantumCircuit(QuantumRegister(1), ClassicalRegister(2))

# Prepare the qubit
qc.h(0)

# First measurement
qc.measure(0, 0)
# Second measurement
qc.measure(0, 1)

simulator = AerSimulator()

shots = int(argv[1]) if len(argv) >= 2 else 1000
job = simulator.run(qc, shots=shots)

result = job.result()
counts = result.get_counts()

print(f"Results ({shots} shots): {counts}")