for i in range(1,10):
    for j in range(1,10):
        if not (i % 2 and i % 3) == 0 and i * j < 50:
            print(f"{i}x{j}={i*j}")