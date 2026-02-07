import random, math

def qubit_collapse(cmd, shots=1024):
    # Sim H-gate + measure
    outer = random.choice([0,1])
    inner = random.choice([0,1])
    outcome = f"{outer}{inner}"
    prob = math.sin(math.pi * random.random())**2 * 100  # Bloch sphere
    print(f"Qubit ∞ '{cmd}': {outcome} -> PROFIT ${int(prob*100)} 16.02, prob {prob:.1f}%")
    return outcome

if __name__ == "__main__":
    cmd = input("Команда коллапса: ") or "avito"
    qubit_collapse(cmd)
