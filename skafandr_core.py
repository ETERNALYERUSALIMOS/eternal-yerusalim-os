import qiskit
from qiskit import QuantumCircuit, Aer, execute
import sys, random

def qubit_collapse(command):
    n_qubits = 2
    qc = QuantumCircuit(n_qubits, n_qubits)
    qc.h(range(n_qubits))
    qc.measure(range(n_qubits), range(n_qubits))
    result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1).result()
    counts = result.get_counts()
    outcome = list(counts.keys())[0]
    print(f"Qubit collapse '{command}': {outcome} -> PROFIT ∞")
    return outcome

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "avito"
    qubit_collapse(cmd)
