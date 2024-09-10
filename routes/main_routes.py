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

@router.get("/entrar/esquecisenha", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/entraresquecisenha.html", {"request": request})

@router.get("/feed", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/feed.html", {"request": request})

@router.get("/index", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/produtos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtos.html", {"request": request})

@router.get("/sejaartesao/tipoloja", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/tipodeloja.html", {"request": request})

@router.get("/carrinho", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/carrinho.html", {"request": request})

@router.get("/suporte", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/suporte.html", {"request": request})

@router.get("/produtosparacasa", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtosCasa.html", {"request": request})

@router.get("/produtosparacorpo", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/produtosCorpo.html", {"request": request})

@router.get("/gruposcomunidades", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/gruposComunidades.html", {"request": request})

@router.get("/categorias", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/categorias.html", {"request": request})

@router.get("/materiaprima", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/materiaPrima.html", {"request": request})

@router.get("/regioes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/regioes.html", {"request": request})

@router.get("/destaques", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/destaques.html", {"request": request})

@router.get("/perfilloja", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/perfilLoja.html", {"request": request})