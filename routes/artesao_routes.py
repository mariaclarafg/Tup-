from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/artesaos")
templates = obter_jinja_templates("templates/artesaos")


@router.get("/cadastro/fornecerinformacoescnpj", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cadastro/fornecerinformacoescnpj.html", {"request": request})

@router.get("/cadastro/fornecerinformacoescpf", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cadastro/fornecerinformacoescpf.html", {"request": request})

@router.get("/centraldoartesao/listadetarefas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/listatarefas.html", {"request": request})

@router.get("/centraldoartesao/finalizar", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/finalizar.html", {"request": request})