from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime as dt
import time
import os
import rocketlc.space_schedulle_launch as sll
from fastapi import Request
from src.utils.cors_response import response_in_cors
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
import uvicorn

templates = Jinja2Templates(directory="src/views")



class LaunchInfo(BaseModel):
    name: str
    mission: str
    empire: str
    datetime: str
    location: str
    res_seconds: int
    hour: str
    date: str
    img_url: str



app = FastAPI(debug=True)
origins = ["*"]

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def custom_swagger_ui_html(request:Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "openapi_url": app.openapi_url},
    )


@app.get('/api/ssl', response_model=List[LaunchInfo], summary="Obter informações de lançamentos", tags=["SSL"])
async def ssl_info(request: Request):
    data_launch = sll.launchs()
    return JSONResponse(data_launch)




@app.get("/doc", response_class=HTMLResponse)
async def get_custom_doc(request: Request):
    # Gerar a documentação padrão do FastAPI
    openapi = get_openapi(
        title="My Custom API",
        version="1.0.0",
        description="API Documentation",
        routes=app.routes,
    )
    # Converter a documentação para um HTML
    body = f"<pre>{openapi}</pre>"  # Aqui, você pode customizar como quiser
    # Renderizar o template com a documentação
    return templates.TemplateResponse("doc.html", {"request": request, "body": body})





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run('main:app', host="0.0.0.0", port=port, reload=True)

