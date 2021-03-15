for n in range(1, 101):
    if n > 2:
        if n % 2 == 0:
            continue
    if n > 3:
        if n % 3 == 0:
            continue
    if n > 5:
        if n % 5 == 0:
            continue
    if n > 7:
        if n % 7 == 0:
            continue

    print(n)
