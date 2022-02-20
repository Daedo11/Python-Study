# 집합 자료형
s1 = set([1,2,3])
print(s1)
s2 = set("hello")
print(s2)

# 순서가 없는 집합 자료형을 리스트나 튜플로 변환
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

# 교집합, 합집합, 차집합 구하기
s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])
print(s3 & s4)
print(s3.intersection(s4))
print(s3 | s4)
print(s3.union(s4))
print(s3 - s4)
print(s4 - s3)
print(s3.difference(s4))
print(s4.difference(s3))

# 집합 자료형 관련 함수 (값 1개 추가하기, 여러 개 추가하기, 특정 값 제거)
s5 = set([1, 2, 3])
s5.add(4)
print(s5)
s5.update([4, 5, 6])
print(s5)
s5.remove(2)
print(s5)
