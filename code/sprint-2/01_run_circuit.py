from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Build the circuit
qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)

# Execute the circuit
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)

# Retrieve the results
result = job.result()
counts = result.get_counts()

print(counts)