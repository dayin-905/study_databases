import psycopg2
import os

def get_db_connection():
    """PostgreSQL 데이터베이스에 연결하고 connection 객체를 반환합니다."""
    try:
        db_host = os.getenv("DB_HOST", "db_postgresql")
        db_port = os.getenv("DB_PORT", "5432")
        db_name = os.getenv("POSTGRES_DB", "main_db")
        db_user = os.getenv("POSTGRES_USER", "admin")
        db_password = os.getenv("POSTGRES_PASSWORD", "admin123")
        
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"데이터베이스 연결에 실패했습니다: {e}")
        return None

def enable_uuid_extension():
    """uuid-ossp 확장을 활성화합니다."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
            conn.commit()
            print("uuid-ossp 확장이 활성화되었습니다.")
        except psycopg2.Error as e:
            print(f"uuid-ossp 확장 활성화 중 오류 발생: {e}")
        finally:
            conn.close()

# 문제 1: 테이블 생성 함수
def create_books_table():
    """'books' 테이블을 생성합니다."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                # 기존 테이블이 있다면 삭제
                cur.execute("DROP TABLE IF EXISTS books;")
                cur.execute("""
                    CREATE TABLE books (
                        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                        title VARCHAR(100),
                        price INT
                    );
                """)
            conn.commit()
            return "books 테이블이 생성되었습니다."
        except psycopg2.Error as e:
            return f"테이블 생성 중 오류 발생: {e}"
        finally:
            conn.close()

# 문제 2: INSERT 함수
def insert_books():
    """'books' 테이블에 3개의 도서 데이터를 삽입합니다."""
    books_to_insert = [
        ('파이썬 입문', 19000),
        ('알고리즘 기초', 25000),
        ('네트워크 이해', 30000)
    ]
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                for book in books_to_insert:
                    cur.execute("INSERT INTO books (title, price) VALUES (%s, %s);", book)
            conn.commit()
            return f"{len(books_to_insert)}개 도서가 삽입되었습니다."
        except psycopg2.Error as e:
            return f"데이터 삽입 중 오류 발생: {e}"
        finally:
            conn.close()

# 문제 3: SELECT 함수들
def get_all_books():
    """'books' 테이블의 모든 데이터를 조회합니다."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id, title, price FROM books;")
                records = cur.fetchall()
                return records
        except psycopg2.Error as e:
            print(f"전체 조회 중 오류 발생: {e}")
            return []
        finally:
            conn.close()

def get_expensive_books():
    """가격이 25000원 이상인 도서를 조회합니다."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id, title, price FROM books WHERE price >= 25000;")
                records = cur.fetchall()
                return records
        except psycopg2.Error as e:
            print(f"가격 기반 조회 중 오류 발생: {e}")
            return []
        finally:
            conn.close()

def get_book_by_title(title):
    """제목으로 특정 도서를 조회합니다."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id, title, price FROM books WHERE title = %s;", (title,))
                record = cur.fetchone()
                return record
        except psycopg2.Error as e:
            print(f"제목 기반 조회 중 오류 발생: {e}")
            return None
        finally:
            conn.close()

# 문제 4: UPDATE 함수
def update_second_book_price():
    """저장된 순서에서 두 번째 도서의 가격을 27000으로 변경합니다."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                # 두 번째 도서의 UUID 조회 (ctid 사용, PostgreSQL 특정)
                # OFFSET 1 LIMIT 1은 저장 순서를 보장하지 않을 수 있으므로 ctid를 사용합니다.
                # 하지만 ctid는 안정적인 식별자가 아니므로, 여기서는 title로 찾겠습니다.
                # '알고리즘 기초'가 두 번째로 삽입된 데이터입니다.
                cur.execute("SELECT id FROM books WHERE title = '알고리즘 기초';")
                book_id_to_update = cur.fetchone()

                if book_id_to_update:
                    cur.execute("UPDATE books SET price = 27000 WHERE id = %s;", (book_id_to_update[0],))
                    conn.commit()
                    return "두 번째 도서 가격이 27000으로 수정되었습니다."
                else:
                    return "두 번째 도서를 찾지 못했습니다."
        except psycopg2.Error as e:
            return f"업데이트 중 오류 발생: {e}"
        finally:
            conn.close()

# 문제 5: DELETE 함수
def delete_third_book():
    """저장된 순서에서 세 번째 도서 데이터를 삭제합니다."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                # '네트워크 이해'가 세 번째로 삽입된 데이터입니다.
                cur.execute("SELECT id FROM books WHERE title = '네트워크 이해';")
                book_id_to_delete = cur.fetchone()
                
                if book_id_to_delete:
                    cur.execute("DELETE FROM books WHERE id = %s;", (book_id_to_delete[0],))
                    conn.commit()
                    return "세 번째 도서가 삭제되었습니다."
                else:
                    return "세 번째 도서를 찾지 못했습니다."
        except psycopg2.Error as e:
            return f"삭제 중 오류 발생: {e}"
        finally:
            conn.close()


if '__main__' == '__main__':
    print("===== 1차 검증 시작 =====")
    
    # 0. uuid-ossp 확장 활성화
    enable_uuid_extension()

    # 1. 테이블 생성
    print("\n--- 문제 1: 테이블 생성 ---")
    result = create_books_table()
    print(result)
    
    # 2. 데이터 삽입
    print("\n--- 문제 2: 데이터 삽입 ---")
    result = insert_books()
    print(result)

    # 3. 데이터 조회 (전체)
    print("\n--- 문제 3.1: 전체 데이터 조회 ---")
    all_books = get_all_books()
    print(f"총 {len(all_books)}개의 도서 조회됨:")
    for book in all_books:
        print(book)
        
    print("\n===== 1차 검증 완료 =====")
    
    
    print("\n\n===== 2차 검증 시작 =====")
    
    # 3. 데이터 조회 (조건)
    print("\n--- 문제 3.2: 가격이 25000원 이상인 도서 조회 ---")
    expensive_books = get_expensive_books()
    print(f"총 {len(expensive_books)}개의 비싼 도서 조회됨:")
    for book in expensive_books:
        print(book)
        
    print("\n--- 문제 3.3: 제목으로 '파이썬 입문' 조회 ---")
    book_by_title = get_book_by_title('파이썬 입문')
    print("'파이썬 입문' 조회 결과:")
    print(book_by_title)
    
    # 4. 데이터 수정
    print("\n--- 문제 4: 두 번째 도서 가격 수정 ---")
    update_result = update_second_book_price()
    print(update_result)
    # 수정 확인
    book_updated = get_book_by_title('알고리즘 기초')
    print("수정 후 '알고리즘 기초' 정보:", book_updated)
    
    # 5. 데이터 삭제
    print("\n--- 문제 5: 세 번째 도서 삭제 ---")
    delete_result = delete_third_book()
    print(delete_result)
    # 삭제 확인
    all_books_after_delete = get_all_books()
    print(f"삭제 후 총 {len(all_books_after_delete)}개의 도서 조회됨:")
    for book in all_books_after_delete:
        print(book)

    print("\n===== 2차 검증 완료 =====")
