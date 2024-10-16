from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/artesao")
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_root (request: Request):
    return RedirectResponse("centraldoartesao/listadetarefas", 303)

@router.get("/centraldoartesao/listadetarefas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/listatarefas.html", {"request": request})

@router.get("/cadastro/fornecerinformacoescnpj", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/cadastro/fornecerinformacoescnpj.html", {"request": request})

@router.get("/cadastro/fornecerinformacoescpf", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/cadastro/fornecerinformacoescpf.html", {"request": request})

@router.get("/cadastro/escolhaseuplanopremium/credito", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/cadastro/escolhaseuplanopremiumcredito.html", {"request": request})

@router.get("/cadastro/escolhaseuplanopremium/debito", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/cadastro/escolhaseuplanopremiumdebito.html", {"request": request})

@router.get("/cadastro/escolhaseuplanopremium", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/cadastro/escolhaseuplanopremium.html", {"request": request})

@router.get("/cadastro/compraplanoefetuada", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/cadastro/compraplanoefetuado.html", {"request": request})




@router.get("/centraldoartesao/produtoscadastrados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/produtosCadastrados.html", {"request": request})

@router.get("/centraldoartesao/adicionarprodutos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/addProdutos.html", {"request": request})

@router.get("/centraldoartesao/chat", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/chat.html", {"request": request})

@router.get("/centraldoartesao/revisoes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/revisoes.html", {"request": request})

@router.get("/centraldoartesao/demandas", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/demandas.html", {"request": request})

@router.get("/centraldoartesao/perfildaloja", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/perfilLoja.html", {"request": request})

@router.get("/centraldoartesao/configuracoesloja", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/configuracoesLoja.html", {"request": request})

@router.get("/centraldoartesao/gerenciarAssinatura", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("artesaos/pages/central/gerenciarAssinatura.html", {"request": request})