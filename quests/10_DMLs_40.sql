📌 문제 4 — 키워드 검색 로그 테이블
테이블명: keyword_search_logs
 컬럼:
keyword
result_count
search_time

데이터:
"python", 120, "2025-11-19 10:00:00"
"chatgpt", 300, "2025-11-19 10:05:00"
"docker", 90, "2025-11-19 10:10:00"

👉 요구:
위 3개 데이터를 INSERT
result_count가 100 이상인 키워드 조회
"docker" 검색 결과 수를 150으로 UPDATE
"python" 로그 삭제

CREATE TABLE keyword_search_logs (
    keyword_search_logs_id int,
    keyword varchar(500),
    result_count int,
    search_time varchar(500)
    );

SELECT *
FROM keyword_search_logs;  

INSERT INTO keyword_search_logs (keyword_search_logs_id, keyword, result_count, search_time)
VALUES (1, 'python', 120, '2025-11-19 10:00:00');
INSERT INTO keyword_search_logs (keyword_search_logs_id, keyword, result_count, search_time)
VALUES (2, 'chatgpt', 300, '2025-11-19 10:05:00');
INSERT INTO keyword_search_logs (keyword_search_logs_id, keyword, result_count, search_time)
VALUES (3, 'docker', 90, '2025-11-19 10:10:00');

# 요구 1: result_count가 100 이상인 키워드 조회
SELECT *
FROM keyword_search_logs  
WHERE result_count >= 100;  

# 요구 2: "docker" 검색 결과 수를 150으로 UPDATE
UPDATE keyword_search_logs
SET result_count = 150
WHERE keyword = 'docker';   

# 요구 3: "python" 로그 삭제
DELETE FROM keyword_search_logs WHERE keyword = 'python';