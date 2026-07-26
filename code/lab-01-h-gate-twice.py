from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.h(0)

qc.measure(0, 0)

print(qc)

sim = AerSimulator()
job = sim.run(qc, shots=1000)
result = job.result()

print(result.get_counts())