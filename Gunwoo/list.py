from os import remove
from sqlite3 import paramstyle


gunwoo = 100
dongbin = 200
dongjae = 400

array = [100, 200, 400]

# print(array)
# print(len(array))

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

movie_rank.append("베놈") # 베놈을 추가하는 코드다
print(movie_rank)

print(movie_rank[2]) # 세 번째 원소 출력
print(movie_rank[1]) # 2 번째 원소 충력

movie_rank.insert(1, "카게노지 은신술") # 2 번째 원소로 카게노지 은싱술을 삽잎
print(movie_rank)

movie_rank.remove("스플릿") # 스플릿을 없에는 코드다
print(movie_rank)

array = [8, 5, 2, 9, 7, 5, 3]

array.append(5) # 마지막 위치에 5룰추가하는 코드다
print(array)

array.remove(7)
array.remove(9)
print(array)

# max: 최대
# min: 최소
# sum: 합계

# {}: 대괄호
# []: 중괄호
# (): 소괄호

print(max(array))
print(min(array))
print(sum(array))
