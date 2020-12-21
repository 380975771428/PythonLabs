def H(n, i):
    if n == 0: return 1
    if n == 1: return i

    return 2 * (i * H(n - 1, i) - n * H(n - 2, i))

n = int(input("Enter n: "))
summa = 0

for i in range(1, n + 1):
    summa += H(n, i)

print(summa)