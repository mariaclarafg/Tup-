import json
import sqlite3
from typing import Optional
from models.usuario_model import Usuario
from sql.usuario_sql import *
from util.auth import conferir_senha
from util.database import obter_conexao


class UsuarioRepo:
    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, usuario: Usuario) -> Optional[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR_USUARIO,
                    (
                        usuario.nome,
                        usuario.data_nascimento,
                        usuario.cpf,
                        usuario.email,
                        usuario.telefone,
                        usuario.senha,
                        usuario.perfil,
                    ),                    
                )
                if cursor.rowcount > 0:
                    return usuario
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def checar_credenciais(cls, email: str, senha: str) -> Optional[Usuario]:
        with obter_conexao() as db:
            cursor = db.cursor()
            (id, nome, email, perfil, senha_hash) = cursor.execute(
                SQL_CHECAR_CREDENCIAIS, (email,)).fetchone()
            if nome:
                if conferir_senha(senha, senha_hash):
                    return Usuario(id=id, nome=nome, email=email, perfil=perfil)
            return None
        
    @classmethod
    def atualizar_dados(cls, nome: str, email: str, telefone: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_ATUALIZAR_DADOS_PESSOAIS, (nome, email, telefone, email))
            return resultado.rowcount > 0
        
    @classmethod
    def atualizar_senha(cls, email: str, senha: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_ATUALIZAR_SENHA, (senha, email))
            return resultado.rowcount > 0

    @classmethod
    def excluir(cls, id: int) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR_USUARIO, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Usuario]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                if tupla:
                    usuario = Usuario(*tupla)
                    return usuario
                else:
                    return None
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_quantidade(cls) -> int:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return 0

    @classmethod
    def inserir_dados_json(cls):
        if UsuarioRepo.obter_quantidade() == 0:
            with open("sql/usuarios.json", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
                for usuario in usuarios:
                    UsuarioRepo.inserir(Usuario(**usuario))

    @classmethod
    def email_existe(cls, email: str) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_EMAIL_EXISTE, (email,)).fetchone()
                return tupla[0] > 0
        except sqlite3.Error as ex:
            print(ex)
            return False
