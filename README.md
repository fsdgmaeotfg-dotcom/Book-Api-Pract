# Book API Practice

Практическая работа по созданию REST API на FastAPI. Приложение работает с двумя сущностями: категориями и книгами. Данные сохраняются в PostgreSQL, а запросы к базе выполняются через SQLAlchemy.

## Эндпоинты

- `GET /health` - проверка, что сервис запущен.
- `/categories/` - создание, просмотр, изменение и удаление категорий.
- `/books/` - создание, просмотр, изменение и удаление книг.
- `GET /books/?category_id=1` - список книг из выбранной категории.

## Подготовка проекта

1. Создать файл `.env` в корне проекта:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```

2. Создать виртуальное окружение и установить зависимости:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Убедиться, что PostgreSQL запущен:

```bash
pg_isready -h localhost -p 5432
```

## Запуск API

```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

После запуска документация будет доступна по адресу:

- http://127.0.0.1:8000/docs

Проверить работу сервиса можно запросом:

```bash
curl http://127.0.0.1:8000/health
```

## Проверка данных

Таблицы создаются автоматически при старте приложения. После добавления данных через Swagger или curl их можно посмотреть в PostgreSQL:

```sql
SELECT * FROM categories;
SELECT * FROM books;
```

## Скриншоты

В папке `examples/` находятся скриншоты Swagger и успешных запросов к API.
