from sys import argv

from helper_class import QuantumExperimentHandler
from qiskit import (
    ClassicalRegister,
    QuantumCircuit,
    QuantumRegister,
)
from qiskit.circuit.exceptions import CircuitError


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
except ValueError as error:
    print(f"Invalid shots value: {error}")
    raise SystemExit(1)

LESSON_TITLE = "Q5 - X Gate (Quantum NOT) Extra Experiment"

qubits = QuantumRegister(1, "q")
measurements = ClassicalRegister(1, "c")

try:
    qc = QuantumCircuit(qubits, measurements)

    qc.x(0)
    qc.measure(0, 0)
    qc.x(1)
    qc.measure(0, 0)

    experiment = QuantumExperimentHandler()
    experiment.run_experiment(LESSON_TITLE, qc, shots)
except CircuitError as ce:
    print(f"Invalid circuit configuration: {ce}")
    raise SystemExit(2)