📌 문제 5 — 쇼핑몰 상품 테이블
테이블명: shop_products
 컬럼:
name
price
stock
category

데이터:
"USB 메모리", 12000, 50, "전자제품"
"블루투스 스피커", 45000, 20, "전자제품"
"물병", 5000, 100, "생활용품"

👉 요구:
위 데이터로 INSERT문 작성
price가 10000 이상인 상품 조회
"물병"의 stock을 80으로 수정
"블루투스 스피커" 삭제

CREATE TABLE shop_products (
    shop_products_id int,
    name varchar(500),
    price int,
    stock int,
    category varchar(500)
);

SELECT *
FROM shop_products;

INSERT INTO shop_products (shop_products_id, name, price, stock, category)
VALUES (1, 'USB 메모리', 12000, 50, '전자제품');
INSERT INTO shop_products (shop_products_id, name, price, stock, category)
VALUES (2, '블루투스 스피커', 45000, 20, '전자제품');
INSERT INTO shop_products (shop_products_id, name, price, stock, category)
VALUES (3, '물병', 5000, 100, '생활용품');

# 요구 1: price가 10000 이상인 상품 조회
SELECT *
FROM shop_products
WHERE price >= 10000;

# 요구 2: "물병"의 stock을 80으로 수정
UPDATE shop_products
SET stock = 80
WHERE name = '물병';

# 요구 3: "블루투스 스피커" 삭제
DELETE FROM shop_products
WHERE name = '블루투스 스피커';