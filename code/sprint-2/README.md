# Sprint 2 – Executing Quantum Circuits

## Objectives

- [X] Execute quantum circuits using AerSimulator
- [X] Understand job, result, and counts
- [X] Interpret deterministic vs. probabilistic results
- [X] Analyze measurement distributions
- [X] Build reusable helper functions for future sprints
- [X] Compared multiple circuits
- [X] Created a reusable QuantumExperimentHandler
- [X] Learned how shots affect measurements
- [X] Analyzed counts and converted them into probabilities

## Questions Answered

| Lesson | Question Answered |
|--------|-------------------|
| 01 | How do I execute circuits? |
| 02 | How do I inspect the results returned by Qiskit? |
| 03 | How do different quantum gates affect measurement outcomes? |
| 04 | How can I reuse code to run quantum experiments? |
| 05 | Why do quantum programmers run the same circuit multiple times? |
| 06 | How do I interpret measurement results? |

## Experiment Outputs

__Note__: See lesson 4...

```bash
==================================================
Experiment: Hadamard Gate
==================================================

Circuit
-------
<diagram>

Execution
---------
Shots: 1000

Results
-------
{'0': 503, '1': 497}

Observations
------------
The measurements are approximately evenly split.
```

## Pro Tips

### Python Engineering Tip #1

When exploring a new library, don't rely solely on IDE hovers. Use:
```python
print(type(obj))
print(dir(obj))
help(obj)
```

### Python Engineering Tip #2

Use `pprint()` when inspecting nested dictionaries:
```python
from pprint import pprint
...
pprint(result.__dict__)      # if available
pprint(result.to_dict())     # if available
```

### Python Engineering Tip $3

Use `help()` to inspect documentation:
```python
help(result)
```