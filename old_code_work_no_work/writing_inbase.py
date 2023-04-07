# from typing import Any, Generic, Type, TypeVar
#
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from db.db_coonection import Base, get_session
#
# ModelType = TypeVar('ModelType', bound=Base)
# CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
#
#
# class Repository:
#
#     def get(self, *args, **kwargs):
#         raise NotImplementedError
#
#
# class RepositoryDB(Repository, Generic[ModelType, CreateSchemaType]):
#
#     def __init__(self, model: Type[ModelType]):
#         self._model = model
#
#     async def get(self, db: AsyncSession, id):
#         statement = select(self._model).where(self._model.id == id)
#         results = await db.execute(statement=statement)
#         return results.scalar_one_or_none()
#
#
#
# from models.models import Publisher, Platform, Game
# from schemas.schemas import PublisherCreate, PlatformCreate, GenreCreate
#
# class RepositoryPublisher(RepositoryDB[Publisher, PublisherCreate]):
#     pass
#
#
# publisher_crud = RepositoryPublisher(Publisher)
# db: AsyncSession = get_session()
# publ = publisher_crud.get(db, 1)
# print(publ)
# # @router.get('/user/{id}', response_model=user_schema.User, tags=['user crud'])
# # async def get_user_by_id(*, db: AsyncSession = Depends(get_session), id) -> Any:
# #     user = await user_crud.get(db=db, id=id)
# #     if not user:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='users by id not found')
# #     return user
#
# # def main():
# #     statement = 'INSERT INTO platform name) VALUES ("me")'
#     # await database.execute(query=statement)
#
#
# # if __name__ == '__main__':
# #     main()
# #

