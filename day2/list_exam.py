# 리스트 연산
arr = list(range(5))        # [0, 1, 2, 3, 4]
print(arr)

arr = list(range(1, 6))      # [1, 2, 3, 4, 5]
print(arr)

arr = list(range(2, 101, 2))
print(arr)

print(arr[0] + arr[5])       # 14

# 2차원 배열 리스트
print()
arr2 = [1, 2, ['Hi', 'My', 'Friend']]
print(arr2[0])
print(arr2[2])
print(arr2[2][1])
print(arr2[2][1][0])

arr3 = list(range(1, 4))
print(arr3)
print(arr3 * 4)
print(arr3 + arr)
# print(arr3 + 3)          배열에다 3을 더할 수 없다

print(len(arr))

# 리스트 함수
print('-- 리스트 내장함수 -- ')
del(arr3[1])
print(arr3)

arr3.remove(1)
print(arr3)

# 리스트 삭제
arr4 = [4, 2, 6, 9, 12, 16, 7, 1, 3, 3, 5]
arr4.remove(3)                # 값을 찾아서 삭제
print(arr4)                   # 최초의 3 하나만 지워짐
del(arr4[8])                  # 리스트의 인덱스로 삭제
print(arr4)

# 리스트 정렬, 역정렬
arr4.sort()
print(arr4)

arr4.reverse()
print(arr4)

# 어디 위치에 무언가를 넣음
arr4.insert(2, 10)            # 2번째 인덱스 위치에 10을 넣겠다
print(arr4)

arr4[0] = 108
print(arr4)

# 튜플
tup1 = tuple(range(1, 6))
print(tup1)
print(tup1[3])

# tup1[0] = 99                # 튜플은 값을 바꿀 수 없다
# print(tup1)
# tup1.remove() -> 튜플은 remove() 자체가 없음

# 딕셔너리
dic1 = { 1: 'a'}
dic1[2] = 'b'
print(dic1)

dic1['name'] = 'Hugo'
print(dic1)

del dic1['name']
print(dic1)

print(dic1.keys())            # dict_keys([1, 2])
print(dic1.values())          # dict_values(['a', 'b'])
print(dic1.items())           # dict_items([(1, 'a'), (2, 'b')])

# 리스트를 튜플로 변환
print('-- 리스트 / 튜플 변환 --')
print(arr4)
tup2 = tuple(arr4)            # 튜플로 변환
print(tup2)

arr4.sort()

# 내가 튜플에 값을 넣고 싶다면, 리스트로 바꾼 뒤 넣어줌
print(tup1)
arr5 = list(tup1)
print(arr5)
arr5.append(6)
print(arr5)
tup1 = tuple(arr5)
print(tup1)