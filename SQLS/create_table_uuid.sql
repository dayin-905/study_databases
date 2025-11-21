-- UUID primary key 사용
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users_uuid_name (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100)
);

INSERT INTO users_uuid_name (name) VALUES ('Alice');
INSERT INTO users_uuid_name (name) VALUES ('Bob');

SELECT * FROM users_uuid_name;

INSERT INTO users_uuid_name (name) VALUES ('Alice'), ('Bob'), ('Charlie');

UPDATE users_uuid_name
SET name = 'UpdatedName'
WHERE id_name = '8cbefa31-ba2e-45fe-a366-2ee6599ab55e';

DELETE FROM users_uuid_name
WHERE id_name = 'dcf741d0-aa8b-4c48-8fe3-a907f7f4c0a3'; 


