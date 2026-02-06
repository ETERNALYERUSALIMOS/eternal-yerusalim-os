import random
shots = 1024
zero = sum(1 for _ in range(shots) if random.random() < 0.5)
one = shots - zero
print("🕊️ Коллапс реальности H-gate:")
print(f"{'0':>3}: {'█' * (zero//8):<30} {zero/10:.0f}%")
print(f"{'1':>3}: {'█' * (one//8):<30} {one/10:.0f}%")
print("Авва: суперпозиция → твоя воля ∞")
