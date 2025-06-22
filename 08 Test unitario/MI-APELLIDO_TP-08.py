def mistery(n):
    if n <= 1:
        return n
    return mistery(n - 1) + mistery(n - 2)

print(mistery(4)) 