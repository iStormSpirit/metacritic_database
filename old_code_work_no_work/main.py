# import uvicorn
# from fastapi import FastAPI
# from fastapi.responses import ORJSONResponse
#
# # from api import base
# # from core.config import app_settings
#
# app = FastAPI(
#     title='game_roulette',
#     docs_url='/api/openapi',
#     openapi_url='/api/openapi.json',
#     default_response_class=ORJSONResponse,
# )
#
# app.include_router(base.api_router)
#
# if __name__ == '__main__':
#     uvicorn.run(
#         'main:app',
#         host='0.0.0.0',
#         port=8000,
#     )