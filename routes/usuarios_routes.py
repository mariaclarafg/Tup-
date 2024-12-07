from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from models.usuario_model import Usuario


router = APIRouter(prefix="/usuario")

templates = Jinja2Templates(directory="templates")



@router.get("/alteraremail", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("usuarios/alterarEmail.html", {"request": request})

@router.get("/alterarsenha", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("usuarios/alterarSenha.html", {"request": request})

@router.get("/alterarnome", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("usuarios/alterarNome.html", {"request": request})

@router.get("/alterardata", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("usuarios/alterarData.html", {"request": request})

@router.get("/alterartelefone", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("usuarios/alterarTelefone.html", {"request": request})


@router.get("/cancelar", response_class=HTMLResponse)
async def get_cancelar(request: Request):
    usuario = request.state.usuario
    if not usuario:
        return RedirectResponse("/entrar", 303)
    nome_perfil = None
    match (usuario.perfil):
        case 1: nome_perfil = "cliente"
        case 2: nome_perfil = "artesao"
        case 3: nome_perfil = "administrador"
        case _: nome_perfil = ""
    return_url = f"/{nome_perfil}"
    response = RedirectResponse(return_url, status_code=status.HTTP_303_SEE_OTHER)
    return response