# 변수 - 자료형의 값을 저장하는 공간

a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
print(a is b)

a[1] = 4
print(a)
print(b)

c = [1, 2, 3]
d = c[:]
c[1] = 4
print(c)
print(d)

from copy import copy
e = [1, 2, 3]
f = copy(e)
print(e)
print(f)
print(b is a)

# 변수를 만드는 여러 가지 방법
g = 3
h = 5
g, h = h, g
print(g)
print(h)

# 변수 i와 j는 서로 다른 메모리를 가리키므로 False
i = [1, 2, 3]
j = [1, 2, 3]
print(i is j)
