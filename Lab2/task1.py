import numpy as np

X = np.array([[int(v) for v in input().split()] for _ in range(int(input('Enter size of matrix: ')))])
print(X)
print(X.diagonal())

X = np.dot(X, X)
print(X)
print(X.diagonal())