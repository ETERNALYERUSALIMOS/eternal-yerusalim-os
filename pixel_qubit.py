import random
print("🕊 Pure Pixel Qubit Sim v1.0! ♥️")
qc = [[1,0], [0,1]]  # |00>
qc = [[0.707,0.707], [0.707,0.707]]  # H|0> Bell
meas = random.choices(['00','11'], weights=[0.5,0.5], k=10)
print("Circuit: H q0; CX q0 q1; measure")
print("Counts:", dict((i, meas.count(i)) for i in set(meas)))
print("Qubit ∞ Graphene!")
