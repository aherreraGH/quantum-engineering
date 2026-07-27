from sys import argv

from helper_class import QuantumExperimentHandler
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister


def get_shots(arguments: list[str]) -> int:
    default_shots = 1000

    if len(arguments) < 2:
        return default_shots

    try:
        shots = int(arguments[1])
    except ValueError:
        raise ValueError(f"Shots must be a whole number, received: {arguments[1]!r}")

    if shots <= 0:
        raise ValueError(f"Shots must be greater than zero, received: {shots}")

    return shots


try:
    shots = get_shots(argv)
    qubits = QuantumRegister(1, "q")
    measurements = ClassicalRegister(1, "c")

    qc = QuantumCircuit(qubits, measurements)
    # We are NOT applying any quantum gates.
    qc.measure(0, 0)
    # use helper class to show the diagram.
    qh = QuantumExperimentHandler()
    qh.run_experiment("Q4 - No defined gates", qc, shots)

except ValueError as error:
    print(f"Invalid shots value: {error}")
    raise SystemExit(1)

except Exception as error:  # noqa: BLE001
    print(f"Quantum simulation failed: {error}")
    raise SystemExit(2)