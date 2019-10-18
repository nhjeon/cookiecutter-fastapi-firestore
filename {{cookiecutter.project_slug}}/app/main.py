from fastapi import FastAPI

from api import api_router

app = FastAPI()  # pylint: disable=invalid-name
app.include_router(api_router)
