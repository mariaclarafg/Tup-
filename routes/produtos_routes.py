from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/produtos")
templates = obter_jinja_templates("templates/produtos")


@router.get("/produtosparacasa", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtosCasa.html", {"request": request})

@router.get("/gruposcomunidades", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/gruposComunidades.html", {"request": request})

@router.get("/portachaves", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtoDetalhes_PortaChaves.html", {"request": request})

@router.get("/vasoceramica", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtoDetalhes_VasoCeramica.html", {"request": request})

@router.get("/quadrobordado", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtoDetalhes_QuadroBordado.html", {"request": request})

@router.get("/bordado", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtoDetalhes_Bordado.html", {"request": request})