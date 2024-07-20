memory_eater = []
try:
    while True:
        memory_eater.append('A' * 10**6)  # Append a 1 MB string to the list
except MemoryError:
    print("Memory exhausted!")
