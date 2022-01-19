# 파일 입출력

# 파일 출력
# f = open('newfile.txt', 'w')   # 써서 없더 파일이 생기니까 출력이다 (입력 아님)
# f.close()  # open()하면 close() 필수. 큰일남

# 특정경로에 파일 생성
# f = open('C:/Sources/Sample/text2.txt', 'w')
# f.close()
# print('파일이 생성되었습니다.')

# ascii (영어만 처리), cp949(한글처리), utf-8 

# newfile.txt 파일입력(읽어오기)
f = open('newfile.txt', 'r', encoding = 'utf-8')
# while True:
#     line = f.readline()
#     if not line : 
#         break
    
#     print(line)

# f.close()

lines = f.readlines()
for line in lines:
    print(line)

f.close()