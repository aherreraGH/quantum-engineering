from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from sys import argv

qc = QuantumCircuit(1, 1)

# Prepare the qubit
qc.h(0)

# Measure it
qc.measure(0, 0)

simulator = AerSimulator()

shots = int(argv[1]) if len(argv) >= 2 else 1000
job = simulator.run(qc, shots=shots)

result = job.result()
counts = result.get_counts()
print(f"Results ({shots} shots): {counts}")

# Debugging, with pro tips...
# help(AerSimulator.run)
# help(result.get_counts)
# help(QuantumCircuit.h)

"""
Observation

With a small number of shots, the measured distribution can vary 
significantly from the expected probabilities. As the shot count 
increases, the observed frequencies converge toward the Hadamard 
state's theoretical 50/50 measurement probabilities.
"""