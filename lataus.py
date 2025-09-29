import sys, time

for i in range(0, 101, 2):
    bar = "█" * (i // 5) + "░" * (20 - i // 5)
    sys.stdout.write(f"\rAloitetaan ohjelmaa: [{bar}] {i}%")
    sys.stdout.flush()
    time.sleep(0.1)
print("\nValmis!")