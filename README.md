# Book API Practice

API для учебного проекта с книгами и категориями. Приложение написано на FastAPI, данные хранятся в PostgreSQL, работа с таблицами идет через SQLAlchemy.

## Что есть в проекте

- категории книг: создание, просмотр, редактирование и удаление;
- книги: создание, просмотр, редактирование и удаление;
- фильтр книг по категории через `category_id`;
- Swagger-документация для ручной проверки запросов.

## Настройка

Создайте `.env` в корне проекта:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```

Установите зависимости:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Проверьте, что PostgreSQL запущен:

```bash
pg_isready -h localhost -p 5432
```

## Запуск

```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

После запуска:

- Swagger: http://127.0.0.1:8000/docs
- Проверка API: http://127.0.0.1:8000/health

## Проверка в базе

После создания данных через API можно проверить таблицы:

```sql
SELECT * FROM categories;
SELECT * FROM books;
```

Скриншоты для сдачи находятся в папке `examples/`.
