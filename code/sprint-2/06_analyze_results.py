from qiskit import QuantumCircuit

from helper_class import QuantumExperimentHandler

qh = QuantumExperimentHandler()

circuit_a = QuantumCircuit(1, 1)
circuit_a.measure(0, 0)

circuit_b = QuantumCircuit(1, 1)
circuit_b.x(0)
circuit_b.measure(0, 0)

circuit_c = QuantumCircuit(1, 1)
circuit_c.h(0)
circuit_c.measure(0, 0)

qh.run_experiment("Experiment A", circuit_a)
qh.run_experiment("Experiment B", circuit_b)
qh.run_experiment("Experiment C", circuit_c)