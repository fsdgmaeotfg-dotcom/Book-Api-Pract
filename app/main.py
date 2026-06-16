from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import books, categories
from app.db.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Books API",
    description="API для работы с книгами и категориями",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.include_router(categories.router)
app.include_router(books.router)


@app.get("/")
def read_root():
    """Главная страница API"""
    return {"message": "Books API v1.0", "docs": "/docs"}


@app.get("/health")
def health_check():
    """Проверка здоровья сервиса"""
    return {"status": "healthy", "service": "Books API"}
