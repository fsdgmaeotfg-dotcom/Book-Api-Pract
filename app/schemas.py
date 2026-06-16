from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = None
    price: float = Field(ge=0)
    category_id: int
    url: str | None = Field(default=None, max_length=1024)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = None
    price: float | None = Field(default=None, ge=0)
    category_id: int | None = None
    url: str | None = Field(default=None, max_length=1024)


class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True
