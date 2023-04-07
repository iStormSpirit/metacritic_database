from pydantic import BaseModel


class BaseModelConfig(BaseModel):
    class Config:
        orm_mode = True


class DeveloperBase(BaseModelConfig):
    id: int
    name: str


class DeveloperCreate(BaseModel):
    name: str


class PublisherBase(BaseModelConfig):
    id: int
    name: str


class PublisherCreate(BaseModel):
    name: str


class PlatformBase(BaseModelConfig):
    id: int
    name: str


class PlatformCreate(BaseModel):
    name: str


class GenreBase(BaseModelConfig):
    id: int
    name: str


class GenreCreate(BaseModel):
    name: str


class GameBase(BaseModelConfig):
    id: int
    name: str
    # detail_link: str
    # release_date: str
    # num_players: str
    # meta_score: str
    # description: str


class GameCreate(BaseModel):
    name: str
    # detail_link: str
    # release_date: str
    # num_players: str
    # meta_score: str
    # description: str
