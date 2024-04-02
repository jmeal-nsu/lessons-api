from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from src.core.logger import logger
from src.api import routers

logger.debug("Main app initialization")

app = FastAPI()


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json", title="Realytics Markup API docs"
    )


for router in routers:
    app.include_router(router)
