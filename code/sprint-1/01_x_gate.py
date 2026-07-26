from qiskit import QuantumCircuit
# That simulator lets us develop quantum software on an ordinary laptop
from qiskit_aer import AerSimulator

# Create a quantum circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)
# 0 argument is not a quantity. It identifies which qubit the gate acts on
# The X gate flips the computational state:
#
# |0⟩ → |1⟩
# |1⟩ → |0⟩
#
# It is roughly analogous to a classical NOT operation.
"""
The X gate does have a more descriptive name:

Pauli-X Gate

It is named after Wolfgang Pauli, one of the pioneers of quantum mechanics.
"""
qc.x(0)
# Measure the qubit into the classical bit
qc.measure(0, 0)

# Display the circuit
print(qc)

# Run the simulator
simulator = AerSimulator()

# A shot is one complete execution of the quantum circuit.
# Instead of running once and getting one deterministic answer, 
# quantum programs are often executed repeatedly to build a 
# probability distribution.
job = simulator.run(qc, shots=1000)

result = job.result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)


"""
Notice how much of this already feels familiar.

We have:

an object (QuantumCircuit)
configuration (measure)
an execution engine (AerSimulator)
a job (run)
a result (job.result())
structured output (counts)
"""