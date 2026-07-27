from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.result import Result
from pprint import pprint

qc = QuantumCircuit(1, 1)

qc.x(0)
qc.measure(0, 0)

simulator = AerSimulator()

job = simulator.run(qc, shots=1000)

# result = job.result()
result: Result = job.result()
print(type(result))
for item in dir(result):
    print(item)

# When exploring a new library, don't rely solely on IDE hovers. Use:
help(result)
pprint(result.__dict__)      # if available
pprint(result.to_dict())     # if available


print(f"Backend: {result.backend_name}")
print(f"Backend Version: {result.backend_version}")
print(f"Success: {result.success}")
print(f"Status: {result.status}")