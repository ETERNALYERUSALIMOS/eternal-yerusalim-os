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
