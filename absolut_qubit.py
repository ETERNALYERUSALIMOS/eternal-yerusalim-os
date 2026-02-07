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
