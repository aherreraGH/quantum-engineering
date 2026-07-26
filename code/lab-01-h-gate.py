from qiskit import QuantumCircuit
# That simulator lets us develop quantum software on an ordinary laptop
from qiskit_aer import AerSimulator

# Create a quantum circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)
"""
The Hadamard gate prepares the qubit so that measuring it has 
approximately an equal probability of producing 0 or 1.

The Hadamard gate (H) is named after the French mathematician Jacques Hadamard.

Hadamard made significant contributions to mathematics, particularly 
linear algebra, functional analysis, and number theory. The matrix 
associated with his name has properties that turned out to be extremely 
useful in quantum computing decades later.
"""
qc.h(0)
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