from pydantic import BaseModel


class BaseModelConfig(BaseModel):
    class Config:
        orm_mode = True


class DeveloperBase(BaseModelConfig):
    id: int
    name: str


class PublisherBase(BaseModelConfig):
    id: int
    name: str


class PlatformBase(BaseModelConfig):
    id: int
    name: str


class GenreBase(BaseModelConfig):
    id: int
    name: str


class GameBase(BaseModelConfig):
    id: int
    name: str
    detail_link: str
    release_date: str
    num_players: str
    meta_score: str
    description: str
