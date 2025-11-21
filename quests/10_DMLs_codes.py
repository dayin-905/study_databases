import psycopg2
import os

"""PostgreSQL 데이터베이스에 연결합니다."""
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")

# 📌 문제 2 — CREATE (INSERT) 기초
# ✔ 요구사항
# 위 students 테이블에 다음 데이터를 INSERT 하시오.

# with conn.cursor() as cursor :
#     cursor.execute ("INSERT INTO students (name, age) VALUES ('홍길동', 23), ('이영희', 21), ('박철수', 26);")
#     
# #📌 문제 3 — READ (SELECT) 기본 조회
# 다음 조건들을 만족하는 SELECT 쿼리를 작성하시오.
# - students 테이블의 전체 데이터를 조회
# with conn.cursor() as cursor :
#     cursor.execute ("SELECT * FROM students;")
#     records = cursor.fetchall()

# - 나이가 22세 이상인 학생만 조회
# with conn.cursor() as cursor :
#     cursor.execute ("SELECT name FROM students WHERE age >= 22;")
#     records = cursor.fetchall()
#     for record in records :
#         print(f'나이가 22세 이상인 학생 : {record[0]}')

# - name 이 “홍길동”인 학생만 조회
# with conn.cursor() as cursor :   
    # cursor.execute ("SELECT name FROM students WHERE name = '홍길동';")
    # records = cursor.fetchall()
    # for record in records :
    #     print(f'name이 홍길동인 학생 : {record[0]}')


# 📌 문제 4 — UPDATE 연습
# ✔ 요구사항
# id = 3e31c685-9410-4de2-b0d9-0674a9845da0 인 학생의 나이를 25로 수정하시오.  
with conn.cursor() as cursor :
    cursor.execute ("""UPDATE students
                    SET age = '25'
                    WHERE id = '3e31c685-9410-4de2-b0d9-0674a9845da0';""")

# Option : select 통한 UUID id 가져와서 update


# 📌 문제 5 — DELETE
# #  연습
# # ✔ 요구사항
# # id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.

# with conn.cursor() as cursor :
#     cursor.execute ("DELETE FROM students WHERE id = 0252dbab-8307-469b-ae8e-ca30d92f1d42;")

# # Option : select 통한 UUID id 가져와서 삭제


conn.commit() # 완료