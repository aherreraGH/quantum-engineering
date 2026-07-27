from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()

def execute(circuit: QuantumCircuit, shots: int = 1000):
    job = simulator.run(circuit, shots=shots)
    result = job.result()
    return result.get_counts()

def run_experiment(name: str, circuit: QuantumCircuit):
    """
    run_experiment()
        ├── prints the circuit
        ├── calls execute()
        └── prints the counts
    """
    print("=" * 50)
    print(name)
    print("=" * 50)

    print("\nCircuit")
    print("-------")
    print(circuit)

    counts = execute(circuit)

    print("\nResults")
    print("-------")
    print(counts)
    print()

circuit_a = QuantumCircuit(1, 1)
circuit_a.measure(0, 0)

circuit_b = QuantumCircuit(1, 1)
circuit_b.x(0)
circuit_b.measure(0, 0)

circuit_c = QuantumCircuit(1, 1)
circuit_c.h(0)
circuit_c.measure(0, 0)

run_experiment("Experiment A", circuit_a)
run_experiment("Experiment B", circuit_b)
run_experiment("Experiment C", circuit_c)


circuit_d = QuantumCircuit(1, 1)
circuit_d.h(0)
circuit_d.h(0)
circuit_d.measure(0, 0)

run_experiment("Experiment D", circuit_d)

# Observation on Circuit D:
#
# Applying H once creates an equal superposition.
# Applying H a second time reverses the first Hadamard operation.
# Since the qubit began in |0>, it returns to |0> and measures 0 every time.