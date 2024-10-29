from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/cliente")
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_root (request: Request):
    return RedirectResponse("centroPessoal/perfil", 303)

@router.get("/feedhome", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("feed/pages/feedhome.html", {"request": request})

@router.get("/centroPessoal/perfil", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/perfil.html", {"request": request})

@router.get("/centroPessoal/enderecossalvos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/enderecossalvos.html", {"request": request})

@router.get("/centroPessoal/cartoescadastrados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/cartoescadastrados.html", {"request": request})


@router.get("/centroPessoal/todosospedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/todosospedidos.html", {"request": request})

@router.get("/centroPessoal/pedidosnaopagos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/pedidosnaopagos.html", {"request": request})

@router.get("/centroPessoal/processandopedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/processandopedidos.html", {"request": request})

@router.get("/centroPessoal/devolucaopedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/devolucaopedidos.html", {"request": request})

@router.get("/centroPessoal/pedidosenviados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/pedidosenviados.html", {"request": request})

@router.get("/centroPessoal/avaliacaoprodutos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/avaliacaoprodutos.html", {"request": request})

@router.get("/centroPessoal/pedidosentregues", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/pedidosentregues.html", {"request": request})

@router.get("/centroPessoal/novaavaliacao", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/novaavaliacao.html", {"request": request})

@router.get("/centroPessoal/favoritos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/favoritos.html", {"request": request})

@router.get("/centroPessoal/rastrearprodutos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/rastrearprodutos.html", {"request": request})












