from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()


def execute(circuit: QuantumCircuit, shots: int = 1000):
    job = simulator.run(circuit, shots=shots)
    result = job.result()
    return result.get_counts()

def run_experiment(name: str, circuit: QuantumCircuit):
    print(f"\n{name}")
    print("-" * len(name))

    print(circuit)

    counts = execute(circuit)

    print(counts)


circuit_a = QuantumCircuit(1, 1)
circuit_a.measure(0, 0)

run_experiment("Circuit A", circuit_a)

circuit_b = QuantumCircuit(1, 1)
circuit_b.x(0)
circuit_b.measure(0, 0)

run_experiment("Circuit B", circuit_b)

circuit_c = QuantumCircuit(1, 1)
circuit_c.h(0)
circuit_c.measure(0, 0)

run_experiment("Circuit C", circuit_c)

# circuit_a = QuantumCircuit(1, 1)

# circuit_a.measure(0, 0)

# print("Circuit A")
# print(circuit_a.draw())
# print(execute(circuit_a))

# circuit_b = QuantumCircuit(1, 1)

# circuit_b.x(0)
# circuit_b.measure(0, 0)

# print("\nCircuit B")
# print(circuit_b.draw())
# print(execute(circuit_b))

# circuit_c = QuantumCircuit(1, 1)

# circuit_c.h(0)
# circuit_c.measure(0, 0)

# print("\nCircuit C")
# print(circuit_c.draw())
# print(execute(circuit_c))

# Observations
#
# Circuit A always measures 0.
# Circuit B always measures 1.
# Circuit C produces approximately equal numbers of 0s and 1s.
#
# This suggests the Hadamard gate creates a fundamentally different
# state than the Pauli-X gate.