from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


class QuantumExperimentHandler:
    def __init__(self):
        self.simulator = AerSimulator()
        pass

    def execute(self, circuit: QuantumCircuit, shots: int = 1000):
        job = self.simulator.run(circuit, shots=shots)
        result = job.result()
        return shots, result.get_counts()
    
    def run_experiment(self, name: str, circuit: QuantumCircuit):
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

        shots, counts = self.execute(circuit)

        print("\nResults")
        print("-------")
        print(counts)
        print()

        for state, count in counts.items():
            percentage = (count / shots) * 100
            print(f"{state}: {percentage:.1f}%")
