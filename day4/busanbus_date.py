# 부산버스 노선별 이용건수
import csv

file_name = '부산버스정보.csv'
f = open(file_name, mode = 'r', encoding = 'urf-8')

reader = csv.reader(f, delimiter=',')
next(reader)
for line in reader:
    print(line)

f.close()