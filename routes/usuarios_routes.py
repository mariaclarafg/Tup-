from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import Usuario


router = APIRouter(prefix="/usuario")

templates = Jinja2Templates(directory="templates")



@router.get("/alteraremail", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/alterarEmailArtesao.html", {"request": request})

@router.get("/alterarsenha", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/contaalterarsenha.html", {"request": request})

@router.get("/alterarnome", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/contaalterarnome.html", {"request": request})

@router.get("/alterardata", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("cliente/pages/centroPessoal/contaalterardata.html", {"request": request})
