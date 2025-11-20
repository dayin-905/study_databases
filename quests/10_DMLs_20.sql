-- 📌 문제 2 — 웹사이트 링크 수집 테이블
-- 테이블명: web_links
--  컬럼:
-- link_text
-- link_url
-- category

-- 데이터:
-- "네이버", "https://naver.com", "portal"
-- "구글", "https://google.com", "portal"
-- "깃허브", "https://github.com", "dev"

-- 👉 요구:
-- 데이터 3개를 생성하는 INSERT문 작성
-- category가 "portal"인 링크만 조회
-- "깃허브"의 category를 "code" 로 수정
-- "네이버" 데이터 삭제

CREATE TABLE web_links (
    weblinksid int,
    link_text varchar(500),
    link_url varchar(500),
    category varchar(500)
    );

-- INSERT INTO table_name (column1, column2, column3, ...)
-- VALUES (value1, value2, value3, ...);
INSERT INTO web_links (weblinksid, link_text, link_url, category)
VALUES (1, '네이버', 'https://naver.com', 'portal');
INSERT INTO web_links (weblinksid, link_text, link_url, category)
VALUES (2, '구글', 'https://google.com', 'portal');
INSERT INTO web_links (weblinksid, link_text, link_url, category)
VALUES (3, '깃허브', 'https://github.com', 'dev');

SELECT *
FROM web_links;

# 요구 1: category가 "portal"인 링크만 조회
SELECT *
FROM web_links  
WHERE category = 'portal';  

# 요구 2: "깃허브"의 category를 "code" 로 수정
-- UPDATE persons
-- SET firstname = 'smith', lastname = 'black'
-- WHERE personid = 2;
UPDATE web_links
SET category = 'code'
WHERE link_text = '깃허브';

# 요구 3: "네이버" 데이터 삭제
-- DELETE FROM table_name WHERE condition;
DELETE FROM web_links WHERE link_text = '네이버';