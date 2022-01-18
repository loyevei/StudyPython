# < 기본 for문 >

# arr = list(range(1,100))

# for i in arr :
#     print(f'{i:2.1f}')

# < 튜플로 for문 >

# arr2 = ('me', 'my', 'friend', 'Jane')

# for item in arr2 :
#     print(f'{item:>10}')    # 우측 정렬, 우측 글자 끝에서 10자리 만들어라

# < 합계 for문 >

# numbers = list(range(1, 21, 2))  # 1~10까지

# res = 0
# for item in numbers :
#     res += item

# print(f'{numbers[-1]}까지의 총 합은 {res}입니다.')

# < 홀수, 짝수 구분 >

# numbers = list(range(1, 21))  # 1~20까지

# for item in numbers :
#     if item % 2 != 0 :   # 홀수   = if item % 2 == 1 :  # 홀수
#         print(f'{item}은 홀수')

# < 13이상이면 탈출 break 또는 계속 continue >

# numbers = list(range(1, 21)) 

# for item in numbers :
#     if item == 15 :
#         continue   # break

#     if item % 2 == 1 :
#         print(f'{item}은 홀수')

## < 구구단 >
# print(list(range(2, 10)))

# print('구구단 프로그램')
# for i in range(2, 10) :
#     if i == 7 :
#         continue
#     print(f'{i}단 시작')
#     for j in range(2, 10) :
#         print(F'{i} X {j} = {i*j:2d}', end = ' ')    # end = ' '  -> 한 줄 내리는 대신 스페이스
#     print()  # == print('')
    
# print('구구단 프로그램')
# for i in range(1, 10) :
#     for j in range(2, 10) :
#         print(F'{j} X {i} = {i*j:2d}', end = ' ')   # end = ' '  -> 한 줄 내리는 대신 스페이스
#     print()
# for i in range(2, 10) :
#     print(f'{i}단', end = ' ')

# inline for문
a = [1, 2, 3, 4]
result = [i * 3 for i in a]
print(result)

# 기존 for문
t = []
for i in a :
    t.append(i*3)
print(t)