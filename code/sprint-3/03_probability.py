from sys import argv

from qiskit import (
    ClassicalRegister,
    QuantumCircuit,
    QuantumRegister,
)
from qiskit_aer import AerSimulator


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

    # Prepare the qubit.
    qc.h(0)

    # Measure the qubit and store the result.
    qc.measure(0, 0)

    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()

    print(f"Results ({shots} shots): {counts}")

except ValueError as error:
    print(f"Invalid shots value: {error}")
    raise SystemExit(1)

except Exception as error:
    print(f"Quantum simulation failed: {error}")
    raise SystemExit(2)

"""
The Born Rule

Probability = (magnitude of the amplitude)²

Amplitude:
An amplitude is a number describing how much a quantum state contributes
to the qubit's current state.

Probability:
Probability describes how likely that state is to appear when measured.

Why square the amplitude:
Squaring the magnitude converts the amplitude into a non-negative probability.
For an amplitude of 1/sqrt(2), the probability is 1/2, or 50%.
"""