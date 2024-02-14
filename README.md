# Админ-панель для отелей

----

### Для запуска проекта необходимо:

1) В корне проекта создать файл `.env` со следующим содержанием:
```dotenv
SECRET_KEY='some-secret-key'
DEBUG=1
POSTGRES_DB=some-db-name
POSTGRES_USER=some-user
POSTGRES_PASSWORD=some-password
DB_HOST=postgres
DB_PORT=5432
```
2) Находясь в корне проекта, запустить команды:

`docker-compose --profile apply_migrations up -d --build` - применение миграций

`docker-compose --profile backend up -d --build` - запуск проекта
