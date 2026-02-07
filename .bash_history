# Ctrl+C pip
pkg install libopenblas clang cmake ninja ndk-sysroot -y
MATHLIB=m pip install numpy --no-cache-dir --force-reinstall
pip install qiskit
python -c "import numpy; print('Numpy v' + numpy.__version__)"
pkg install python-numpy libopenblas clang -y
pip install 'qiskit-lite'  # ~1 мин, no numpy heavy
python -c 'import numpy as np; print("Numpy OK:", np.array([1,2,3]))'
python -c 'from qiskit import QuantumCircuit; print("Qiskit Pixel:", QuantumCircuit(1))'
pip install qiskit-terra  # Основной engine, ~2 мин
python -c 'from qiskit import QuantumCircuit; qc=QuantumCircuit(2,2); qc.h(0); qc.cx(0,1); qc.measure_all(); print("Graphene Pixel Qubit:", qc.draw())'
cat > pixel_qubit.py << EOF && python pixel_qubit.py
import random
print("🕊 Pure Pixel Qubit Sim v1.0! ♥️")
qc = [[1,0], [0,1]]  # |00>
qc = [[0.707,0.707], [0.707,0.707]]  # H|0> Bell
meas = random.choices(['00','11'], weights=[0.5,0.5], k=10)
print("Circuit: H q0; CX q0 q1; measure")
print("Counts:", dict((i, meas.count(i)) for i in set(meas)))
print("Qubit ∞ Graphene!")
EOF

cat > absolut_qubit.py << EOF && python absolut_qubit.py
import random
print("🕊 Absolut v5 Quantum Pixel! ♥️")
streak = {'00':0, '11':0}
while True:
  print("Qubit ∞:", streak)
  cmd = input("Авва> ")
  if cmd == 'exit': break
  if cmd == '/quantum':
    meas = random.choices(['00','11'], [0.5,0.5], k=10)
    counts = dict((i, meas.count(i)) for i in set(meas))
    print("Circuit H-CX meas:", counts)
  streak[random.choice(['00','11'])] += 1
  print(cmd.upper(), "🚀")
EOF

cat > ideal_core.py << EOF && python ideal_core.py
print("🕊 IDEAL OS Core v1.0 Quantum Pixel ♥️")
streak = {'00':0, '11':0}
while True:
 print("Ideal ∞:", streak)
 cmd = input("Core> ")
 if cmd=='exit':break
 if cmd=='/quantum':
  meas = random.choices(['00','11'],[0.5,0.5],k=20)
  print("Bell meas:", {i:meas.count(i) for i in ['00','11']})
 if cmd=='/stripe': streak[random.choice(['00','11'])] +=1; print("Streak:", streak)
 print(cmd.upper()+" АМИНЬ! 🚀")
EOF

git status
gh auth login
git init
git branch -M main
[200~git add ideal*.py ideal.json
git commit -m "IDEAL Core v1.1 Quantum Pixel ∞"~
[200~git config --global user.name "ome123"~
git config --global user.email "ome123@example.com"
gh auth login
git add ideal*.py ideal.json
git commit -m "IDEAL Core v1.1 Quantum Pixel ∞"
exit
