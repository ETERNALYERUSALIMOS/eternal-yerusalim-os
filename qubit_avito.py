from qiskit import QuantumCircuit, execute, Aer
qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])
result = execute(qc, Aer.get_backend('qasm_simulator'), shots=1024).result()
counts = result.get_counts()
print("Avito profit: 0k 16.02, prob:", max(counts.values())/1024*100, "%")
