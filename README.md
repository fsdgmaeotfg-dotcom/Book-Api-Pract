# Books API

Учебный API на FastAPI для работы с книгами и категориями. Данные хранятся в PostgreSQL, для работы с базой используется SQLAlchemy.

## Возможности

- CRUD для категорий: `/categories/`
- CRUD для книг: `/books/`
- Фильтрация книг по категории: `/books/?category_id=1`
- Проверка сервиса: `/health`

## Настройка

В корне проекта должен быть файл `.env` с настройками базы:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```

Установите зависимости в виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Перед запуском проверьте, что PostgreSQL работает:

```bash
pg_isready -h localhost -p 5432
```

## Запуск

```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

После запуска откройте:

- Swagger: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Проверка базы

Таблицы создаются автоматически при запуске приложения. После запросов через API данные можно проверить в psql:

```sql
SELECT * FROM categories;
SELECT * FROM books;
```

## Скриншоты

Скриншоты для сдачи лежат в папке `examples/`: Swagger `/docs` и успешный запрос к API.
