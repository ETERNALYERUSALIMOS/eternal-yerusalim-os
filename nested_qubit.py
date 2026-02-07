from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(4,4)  # 2 outer + 2 inner
qc.h([0,1])  # Outer H-gate
qc.cx(0,2); qc.cx(1,3)  # Inner entanglement
qc.measure_all()
result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1).result()
print("∞ в ∞ collapse:", result.get_counts())
