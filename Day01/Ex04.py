# 복합 대입 연산자
A = 10
A += 1                      # A = A + 1
print("A += 1 : ", A)       # 11

A = 10
A -= 1
print("A -= 1 : ", A)

A = 10
A *= 2
print("A *= 2 : ", A)

A = 10
A /= 2
print("A /= 2 : ", A)       # 나누기는 실수로 하고있음

A = 10
A //= 2
print("A //= 2 : ", A)     # -> 이거는 정수로 나온다. 정수나누기 했기 때문에
