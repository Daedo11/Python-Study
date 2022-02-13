odd = [1, 3, 5, 7, 9]
print(odd)

# 리스트에서 인덱싱하기
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])

# 이중 리스트에서 인덱싱하기
b = [1, 2, 3, ["a", "b", "c"]]
print(b)
print(b[0])
print(b[-1])
print(b[3])
print(b[-1][0])
print(b[-1][1])
print(b[-1][2])

# 삼중 리스트에서 인덱싱하기
c = [1, 2,["a", "b", ["life", "is"]]]
print(c[-1][-1][0])
print(c[2][2][0])

# 리스트의 슬라이싱
d = [1, 2, 3, 4, 5]
print(d[0:2])
e = d[:2]
f = d[2:]
print(e)
print(f)

# 중첩된 리스트에서 슬라이싱 하기
g = [1, 2, 3, ["a", "b", "c"], 4, 5]
print(g[2:5])
print(g[3][:2])

# 리스트 연산하기
h = [1, 2, 3]
i = [4, 5, 6]
print(h+i)
print(h*3)
print(len(h))

# 초보자가 실수하기 쉬운 리스트 연산 오류 : 숫자열+문자열 오류 수정
j = [1, 2, 3]
print(str(j[2]) + "hi")

# 리스트의 수정과 삭제
a01 = [1, 2, 3]
a01[2] = 4
print(a01)
del a01[1]
print(a01)

a02 = [1, 2, 3, 4, 5]
del a02[2:]
print(a02)

# 리스트 관련 함수
a03 = [1, 2, 3]
a03.append(4)
print(a03)
a03.append([5, 6])
print(a03)

# 리스트 정렬
a04 = [1, 4, 3, 2]
a04.sort()
print(a04)

a05 = ['a', 'c', 'b']
a05.sort()
print(a05)

# 리스트 뒤집기
a04.reverse()
print(a04)

# 위치 반환
a06 = [1, 2, 3]
print(a06.index(3))
print(a06.index(1))

# 리스트에 요소 삽입 a07[0] 위치에 4 삽입
a07 = [1, 2, 3]
a07.insert(0, 4)
print(a07)

a07.insert(3, 5)
print(a07)

# 리스트 요소 제거
a08 = [1, 2, 3, 1, 2, 3]
a08.remove(3)
print(a08)
a08.remove(3)
print(a08)

# 리스트 요소 끄집어내기
a09 = [1, 2, 3]
a09.pop()
print(a09)
a09.pop(1)
print(a09)

# 리스트에 포함된 요소 x의 개수 세기
a10 = [1, 2, 3, 1]
print(a10.count(1))

# 리스트 확장
a11 = [1, 2, 3]
a11.extend([4,5])
print(a11)
b11 = [6, 7]
a11.extend(b11)
print(a11)
