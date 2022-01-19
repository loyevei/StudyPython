# # 웹페이지 긁어오기
# from urllib.request import Request, urlopen

# req = Request('https://www.naver.com')       # 네이버 웹페이지 요청
# res = urlopen(req)

# print(res.status)         # status : 상태값 / 200 --> 웹페이지를 찾았다 / 404 --> not found

# 외부 request 패키지 추가 설치
# pip install requests
import requests      # request 아님 
url = 'http://www.naver.com'
res = requests.get(url)

# print(res.status_code)
print(res.text)

