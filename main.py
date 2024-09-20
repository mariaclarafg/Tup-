from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes.main_routes import main_routes
from routes.clientes_routes import clientes_routes
from routes.artesao_routes import artesao_routes
from routes.feed_routes import feed_routes
from routes.categorias_routes import categorias_routes
from routes.produtos_routes import produtos_routes
from routes import categorias_routes, clientes_routes, comunidades_routes, feed_routes, main_routes, artesao_routes, produtos_routes

from util.exceptions import configurar_excecoes
from util.auth import checar_autenticacao, checar_autorizacao

UsuarioRepo.criar_tabela()
app = FastAPI(dependencies=[Depends(checar_autorizacao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware("http")(checar_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)
app.include_router(artesao_routes.router)
app.include_router(clientes_routes.router)
app.include_router(produtos_routes.router)
app.include_router(feed_routes.router)
app.include_router(comunidades_routes.router)
app.include_router(categorias_routes.router)