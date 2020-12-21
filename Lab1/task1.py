import math as mt

def formula(x, prev_a):
    return (1/2) * (prev_a + (x / prev_a))

print("Enter x eps: ")
x, eps = (float(v) for v in input().split())

prev_a, now_a, n = x, formula(x, x), 1

while mt.fabs(now_a - prev_a) >= eps:
    prev_a = now_a
    now_a = formula(x, prev_a)
    n += 1

print(f"a[{str(n)}] = " + str(now_a))