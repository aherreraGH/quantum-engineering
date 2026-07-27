# Sprint 3 — Single Qubit States and Measurement

## Objectives

- [X] quantum states
- [X] measurement
    - [X] why measurement is random
    - [X] why measurement destroys information
- [X] probabilities
    - [X] probability vs certainty
    - [X] why more shots improve confidence
- [X] why we cannot "peek" inside a qubit
- [X] how engineers verify quantum hardware

## Questions Answered

| Lesson | Question Answered |
|--------|-------------------|
| 01 | What is a qubit, and how is it different from a classical bit? |
| 01 | Why do we need to measure a qubit to obtain a classical result? |
| 02 | What does the Hadamard gate do to a qubit? |
| 02 | Why doesn't a Hadamard gate always produce the same measurement? |
| 03 | Why do probabilities come from amplitudes instead of being stored directly? |
| 03 | Why are amplitudes squared when calculating measurement probabilities? |
| 04 | What is the default state of a newly created qubit? |
| 04 | Why is measuring an unchanged qubit deterministic? |
| 05 | Why is the result deterministic? |
| 05 | How is the X gate different from the Hadamard gate? |
| 05 | Why is the X gate often compared to a classical NOT gate? |

## Pro Tips

### Python Engineering Tip #4

Install **Ruff**, a fast Python linter and code quality tool. It helps enforce PEP 8 formatting, organizes imports, detects unused code, identifies potential bugs, and encourages Python best practices.

If using Visual Studio Code, install the Ruff extension. Most other IDEs also support Ruff or an equivalent Python linter.

### Python Engineering Tip #5

Catch specific exceptions whenever possible. Careful using the catch-all `Exception`:

```python
except ValueError as error:
    print(f"Invalid shots value: {error}")
    raise SystemExit(1)

except Exception as error:  # noqa: BLE001
    print(f"Quantum simulation failed: {error}")
    raise SystemExit(2)
```

### Python Engineering Tip #6

Reuse helper classes instead of duplicating code.
Review `helper_class.py` for an example.

## Quantum Computing Tips

1. Qubits initialize to |0⟩.
2. Probabilities come from amplitudes.
3. Measure only at the end of a circuit (when appropriate).
