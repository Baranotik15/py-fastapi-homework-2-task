from pydantic import BaseModel
from database.models import MovieStatusEnum
from datetime import date as Date


class GenreSchema(BaseModel):
    id: int
    name: str
    model_config = {"from_attributes": True,}


class ActorSchema(BaseModel):
    id: int
    name: str
    model_config = {"from_attributes": True,}


class CountrySchema(BaseModel):
    id: int
    code: str
    name: str | None = None
    model_config = {"from_attributes": True,}


class LanguageSchema(BaseModel):
    id: int
    name: str
    model_config = {"from_attributes": True,}


class MovieBase(BaseModel):
    name: str
    date: Date
    score: float
    overview: str
    status: MovieStatusEnum
    budget: float
    revenue: float
    country: CountrySchema
    genres: list[GenreSchema]
    actors: list[ActorSchema]
    languages: list[LanguageSchema]


class MovieCreateRequest(BaseModel):
    name: str
    date: Date
    score: float
    overview: str
    status: MovieStatusEnum
    budget: float
    revenue: float
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]


class MovieUpdateRequest(BaseModel):
    name: str | None = None
    date: Date | None = None
    score: float | None = None
    overview: str | None = None
    status: MovieStatusEnum | None = None
    budget: float | None = None
    revenue: float | None = None


class MovieDetailSchema(MovieBase):
    id: int
    model_config = {"from_attributes": True,}


class MovieListItemSchema(BaseModel):
    id: int
    name: str
    date: Date
    score: float
    overview: str
    model_config = {"from_attributes": True,}


class MovieListResponseSchema(BaseModel):
    movies: list[MovieListItemSchema]
    prev_page: str | None = None
    next_page: str | None = None
    total_pages: int
    total_items: int

    model_config = {"from_attributes": True,}
