# from typing import Generic, Type, TypeVar
# from pydantic import BaseModel
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from db.db_coonection import Base
#
# ModelType = TypeVar("ModelType", bound=Base)
# CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
#
#
# class Publisher:
#     def get(self, *args, **kwargs):
#         raise NotImplementedError
#
#     def create(self, *args, **kwargs):
#         raise NotImplementedError
#
#
# class WriteDB(Publisher, Generic[ModelType, CreateSchemaType]):
#     def __init__(self, model: Type[ModelType]):
#         self._model = model
#
#     async def get(self, db: AsyncSession, user_id: int) -> ModelType | None:
#         pass
#
#     async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
#         db_obj = self._model(obj_in)
#         db.add(db_obj)
#         await db.commit()
#         await db.refresh(db_obj)
#         return db_obj
#
#
