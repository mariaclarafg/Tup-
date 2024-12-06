from datetime import date
from fastapi import APIRouter, FastAPI, Form, Query, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, criar_token, obter_hash_senha
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso
from util.templates import obter_jinja_templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/") 
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index.html", {"request": request})


@router.get("/entrar")
async def get_entrar(request: Request, return_url: str = Query(None)):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    if not usuario or not usuario.email:
        return templates.TemplateResponse("main/pages/entrar.html", {"request": request, "return_url": return_url})
    if usuario.perfil == 1:
        return RedirectResponse("/cliente", status_code=status.HTTP_303_SEE_OTHER)
    if usuario.perfil == 2:
        return RedirectResponse("/artesao", status_code=status.HTTP_303_SEE_OTHER)
   

@router.post("/post_entrar")
async def post_entrar(
    return_url: str = Form(None),
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/entrar", status_code=status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "Credenciais inválidas, tente novamente.")
        return response
    token = criar_token(usuario.nome, usuario.email, usuario.perfil)
    nome_perfil = None
    match (usuario.perfil):
        case 1: nome_perfil = "cliente"
        case 2: nome_perfil = "artesao"
        case 3: nome_perfil = "administrador"
        case _: nome_perfil = ""
    if not return_url:
        return_url = f"/{nome_perfil}"
    response = RedirectResponse(return_url, status_code=status.HTTP_303_SEE_OTHER)    
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    adicionar_mensagem_sucesso(response, "Credenciais válidas, login realizado com sucesso.")
    return response

@router.get("/cadastrar")
async def get_cadastrar(request: Request):
    options_comunidades = [
        {"label": "Quilombola", "value": "1"},
        {"label": "Indígena", "value": "2"},
        {"label": "Ribeirinho", "value": "3"},
        {"label": "Paneleiras", "value": "4"},
        {"label": "Bordadeiras", "value": "5"},
        {"label": "Pantaneiros", "value": "6"},
        {"label": "Outro", "value": "7"}]
    return templates.TemplateResponse("main/pages/entrarcadastro.html", {"request": request, "options_comunidades": options_comunidades})

@router.post("/post_cadastrar_cliente")
async def post_cadastrar_cliente(
    nome: str = Form(...),
    data_nascimento: date = Form(...),
    cpf: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...)):
    if senha != confsenha:
        return RedirectResponse("/cadastrar", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        email=email,
        telefone=telefone,
        senha=senha_hash,
        perfil=1)
    UsuarioRepo.inserir(usuario)
    return RedirectResponse("/entrar", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/post_cadastrar_artesao")
async def post_cadastrar_artesao(
    nome: str = Form(...),
    data_nascimento: date = Form(...),
    cpf: str = Form(...),
    tipo_comunidade: str = Form(...),
    cnpj: str =Form(...),
    nome_loja: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...)):
    if senha != confsenha:
        return RedirectResponse("/cadastrar", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        cnpj=cnpj,
        tipo_comunidade=tipo_comunidade,
        nome_loja=nome_loja,
        email=email,
        telefone=telefone,
        senha=senha_hash,
        perfil=2)
    UsuarioRepo.inserir(usuario)
    return RedirectResponse("/entrar", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/sair")
async def get_sair():
    response = RedirectResponse("/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value="",
        max_age=1,
        httponly=True,
        samesite="lax")
    return response    

@router.get("/homeartesao", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/artesaos.html", {"request": request})

@router.get("/feed", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/feed.html", {"request": request})

@router.get("/index", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/index.html", {"request": request})

@router.get("/produtos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/produtos.html", {"request": request})

@router.get("/sejaartesao/tipoloja", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/tipodeloja.html", {"request": request})

@router.get("/carrinho", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/carrinho.html", {"request": request})

@router.get("/suporte", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/suporte.html", {"request": request})

@router.get("/produtosparacasa", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/produtosCasa.html", {"request": request})

@router.get("/produtosparacorpo", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/produtosCorpo.html", {"request": request})

@router.get("/gruposcomunidades", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/gruposComunidades.html", {"request": request})

@router.get("/categorias", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/categorias.html", {"request": request})

@router.get("/materiaprima", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/materiaPrima.html", {"request": request})

@router.get("/regioes", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/regioes.html", {"request": request})

@router.get("/destaques", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/destaques.html", {"request": request})

@router.get("/perfilloja", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/perfilLoja.html", {"request": request})

@router.get("/finalizarpedido", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/finalizarPedido.html", {"request": request})

@router.get("/esquecisenha", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/entraresquecisenha.html", {"request": request})