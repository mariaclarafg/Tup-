from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/artesaos")
templates = obter_jinja_templates("templates/artesaos")


@router.get("/centraldoartesao/listadetarefas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/listatarefas.html", {"request": request})

@router.get("/centraldoartesao/produtoscadastrados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/produtosCadastrados.html", {"request": request})

@router.get("/centraldoartesao/adicionarprodutos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/addProdutos.html", {"request": request})

@router.get("/centraldoartesao/chat", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/chat.html", {"request": request})

@router.get("/centraldoartesao/revisoes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/revisoes.html", {"request": request})

@router.get("/centraldoartesao/demandas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/demandas.html", {"request": request})

@router.get("/centraldoartesao/perfildaloja", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/perfilLoja.html", {"request": request})

@router.get("/centraldoartesao/configuracoesloja", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/configuracoesLoja.html", {"request": request})

@router.get("/centraldoartesao/alteraremail", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/alterarEmailArtesao.html", {"request": request})

@router.get("/centraldoartesao/gerenciarAssinatura", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/central/gerenciarAssinatura.html", {"request": request})