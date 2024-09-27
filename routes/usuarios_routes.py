from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import Usuario


router = APIRouter(prefix="/usuario")

templates = Jinja2Templates(directory="templates")


@router.get("/cadastro/fornecerinformacoescnpj", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cadastro/fornecerinformacoescnpj.html", {"request": request})

@router.get("/cadastro/fornecerinformacoescpf", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cadastro/fornecerinformacoescpf.html", {"request": request})

@router.get("/cadastro/escolhaseuplanopremium/credito", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cadastro/escolhaseuplanopremiumcredito.html", {"request": request})

@router.get("/cadastro/escolhaseuplanopremium/debito", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cadastro/escolhaseuplanopremiumdebito.html", {"request": request})

@router.get("/cadastro/escolhaseuplanopremium", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cadastro/escolhaseuplanopremium.html", {"request": request})

@router.get("/cadastro/compraplanoefetuada", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/cadastro/compraplanoefetuado.html", {"request": request})

@router.get("/entrar/esquecisenha", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/entraresquecisenha.html", {"request": request})
