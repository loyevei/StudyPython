# oracle_data
# cx_oracle 설치 : pip install cx_oracle 
import cx_Oracle as ora

# makedsn('호스트명/ip주소', portnum(번호), '서비스명')
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')     # 내 컴퓨터의 DB의 주소 : localhost
# connect(user, password, dsn, encoding)
conn = ora.connect(user='scott', password='tiger', dsn = dsn, encoding = 'utf-8')

cur = conn.cursor()    # 커서 = 뭘 가리키기 위한 준비

# try : 
#     for row in cur.execute('SELECT * FROM emp'):    # execute = 실행하다, 실행을 커서한테 시킴
#         print(row)                                  # 결과값이 튜플(변동X)로 나옴. 리스트로 나오는 것 아님
# # cur.execute('SELECT COUNT(*) FROM emp')           # 원래 emp 뒤에 ; 있어야 함
# # result = cur.fetchone()
# # print(result)
# except ora.DatabaseError as e :
#     print(f'쿼리문이 잘못되었습니다. 13번라인 확인요 : {e}')
# finally:    
#     cur.close()      # 커서부터 닫고
#     conn.close()     # 커넥트(DB접속) 닫기

try : 
    for row in cur.execute('SELECT * FROM emp;'):   # 원래 emp 뒤에 ; 있어야 함
        print(row)                                  # 결과값이 튜플(변동X)로 나옴. 리스트로 나오는 것 아님
    # cur.execute('SELECT COUNT(*) FROM emp')          # 딱 한 건만 가져옴
    # result = cur.fetchone()
    # print(result)
except ora.DatabaseError as e :
    print(f'쿼리문이 잘못되었습니다. 13번라인 확인요 : {e}')
finally:    
    cur.close()      # 커서부터 닫고
    conn.close()     # 커넥트(DB접속) 닫기