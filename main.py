from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from repositories.usuario_repo import UsuarioRepo
from routes import main_routes
import uvicorn
from util.auth import checar_permissao, middleware_autenticacao
from util.exceptions import configurar_excecoes

UsuarioRepo.criar_tabela()
app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")

@app.get("/")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("index.html", view_model)

@app.get("/conta")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("conta.html", view_model)

@app.get("/conta/esquecisenha")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("contaesquecisenha.html", view_model)

@app.get("/conta/cadastro")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("contacadastro.html", view_model)

@app.get("/cadastro/artesao/tipoloja")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("tipodeloja.html", view_model)

@app.get("/produtos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("produtos.html", view_model)

@app.get("/artesaos")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("artesaos.html", view_model)

@app.get("/cadastro/artesao/fornecerinfocpf")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("fornecerinformacoescpf.html", view_model)

@app.get("/cadastro/artesao/fornecerinfocnpj")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("fornecerinformacoescnpj.html", view_model)


@app.get("/feed")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("feed.html", view_model)


@app.get("/feed/paginainicial")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("feedpaginainicial.html", view_model)

@app.get("/carrinho")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("carrinhovazio.html", view_model)

@app.get("/cadastro/artesao/finalizar")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("cadastroartesaofinalizar.html", view_model)


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8209, reload=True)
