from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates/main")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/entrar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/entrar.html", {"request": request})

@router.get("/artesaos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/artesaos.html", {"request": request})

@router.get("/entrar/cadastro", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/entrarcadastro.html", {"request": request})