-- UUID primary key 사용
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users_uuid_name (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100)
);

INSERT INTO users_uuid_name (name) VALUES ('Alice');

SELECT * FROM users_uuid_name;

INSERT INTO users_uuid_name (name) VALUES ('Alice'), ('Bob'), ('Charlie');

UPDATE users_uuid_name
SET name = 'UpdatedName'
WHERE id_name = '8cbefa31-ba2e-45fe-a366-2ee6599ab55e';

