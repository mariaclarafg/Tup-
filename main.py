from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes.main_routes import router as main_routes
from routes.clientes_routes import router as clientes_routes
from routes.artesao_routes import router as artesao_routes
from routes.feed_routes import router as feed_routes
from routes.categorias_routes import router as categorias_routes
from routes.produtos_routes import router as produtos_routes
from routes.comunidades_routes import router as comunidades_routes
from util.exceptions import configurar_excecoes
from util.auth import checar_autenticacao, checar_autorizacao

UsuarioRepo.criar_tabela()
app = FastAPI(dependencies=[Depends(checar_autorizacao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware("http")(checar_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes)
app.include_router(artesao_routes)
app.include_router(clientes_routes)
app.include_router(produtos_routes)
app.include_router(feed_routes)
app.include_router(comunidades_routes)
app.include_router(categorias_routes)