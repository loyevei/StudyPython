# while문
hit = 0

# while hit < 100 :    # 이 값이 참인 동안
#     hit += 1         # hit = hit + 1

#     if hit > 10 :
#         break 

#     print(f'나무를 {hit}번 찍습니다.')


# for문
for hit in range(0,101) :
    if hit > 9 :
        break

    print(f'나무를 {hit+1}번 찍습니다.')

