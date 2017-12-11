ALTER USER postgres PASSWORD 'postgres_user_password' ;
drop database if exists autogger ;
CREATE DATABASE autogger ;
DO
$body$
BEGIN
   IF NOT EXISTS (
      SELECT *
      FROM   pg_catalog.pg_user
      WHERE  usename = 'postgres_user') THEN

      CREATE ROLE postgres_user LOGIN PASSWORD 'postgres_user_password';
      CREATE USER postgres_user WITH PASSWORD 'postgres_user_password' ;
   END IF;
END
$body$;
ALTER ROLE postgres_user SET client_encoding TO 'utf8' ;
ALTER ROLE postgres_user SET default_transaction_isolation TO 'read committed' ;
ALTER ROLE postgres_user SET timezone TO 'UTC' ;
GRANT ALL PRIVILEGES ON DATABASE autogger TO postgres_user ;
alter role postgres_user superuser;
ALTER USER postgres_user CREATEDB;
drop database if exists test_autogger ;
create database test_autogger ;
grant all privileges on database test_autogger to postgres_user ;
