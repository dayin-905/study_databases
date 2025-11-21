-- 📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
-- 아래 요구사항에 맞는 CREATE TABLE 문을 작성하시오.
-- ✔ 요구사항
-- 테이블명: students
-- 컬럼:
-- id (UUID PRIMARY KEY DEFAULT uuid_generate_v4())
-- name (VARCHAR(50))
-- age (INT)

# students 테이블 드랍하기
DROP TABLE students;

# 테이블 생성
CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50),
    age INT
    );

SELECT * FROM students;

-- CREATE TABLE users_uuid_name (
--   id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
--   name VARCHAR(100)
-- );
SELECT name FROM students WHERE name = '홍길동';

📌 문제 4 — UPDATE 연습
✔ 요구사항
id = 2 인 학생의 나이를 25로 수정하시오.
Option : select 통한 UUID id 가져와서 삭제

UPDATE students
SET age = '25'
WHERE id = '3e31c685-9410-4de2-b0d9-0674a9845da0';

UPDATE persons
SET firstname = 'smith', lastname = 'black'
WHERE personid = 2;

select 통한 UUID id 가져와서 update

SELECT * FROM students WHERE id = UUID;

📌 문제 5 — DELETE 연습
✔ 요구사항
id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.
Option : select 통한 UUID id 가져와서 삭제

DELETE FROM students WHERE id = 0252dbab-8307-469b-ae8e-ca30d92f1d42;

DELETE FROM persons WHERE personid = 3;