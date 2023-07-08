Запуск локального сервера
`python3 src/manage.py runserver`

Если локальный сервер не запускается из-за отсутствующей роли djago, вероятно, сломалась БД. Надо зайти в интерактивный шелл БД и выполнить
`sudo su - postgres`
`psql`

`
CREATE DATABASE django_project_db;
CREATE USER django WITH PASSWORD 'nooNaith3iet';
ALTER ROLE django SET client_encoding TO 'utf8'; 
ALTER ROLE django SET default_transaction_isolation TO 'read committed'; 
ALTER ROLE django SET timezone TO 'Europe/Moscow';

GRANT ALL PRIVILEGES ON DATABASE django_project_db TO django;
\q
`

`sudo -u postgres psql django_project_db`
`GRANT CREATE ON SCHEMA public TO django;`
