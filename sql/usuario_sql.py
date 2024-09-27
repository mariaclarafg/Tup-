SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        perfil INT NOT NULL,        
        token TEXT)
"""

SQL_CHECAR_CREDENCIAIS = """
    SELECT nome, email, perfil, senha
    FROM usuario
    WHERE email = ?
"""

SQL_ATUALIZAR_DADOS = """
    UPDATE usuario
    SET nome = ?, email = ?, telefone = ?
    WHERE email = ?
"""

SQL_ATUALIZAR_SENHA = """
    UPDATE usuario
    SET senha = ?
    WHERE email = ?
"""

SQL_EXCLUIR_USUARIO = """
    DELETE FROM usuario
    WHERE email = ?
"""

SQL_INSERIR_USUARIO = """
    INSERT INTO usuario(id, nome, email, senha, perfil)
    VALUES (?, ?, ?)
"""


SQL_ALTERAR_TOKEN = """
    UPDATE usuario
    SET token=?
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, email, perfil, token
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_EMAIL = """
    SELECT id, nome, email, perfil, token
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_TOKEN = """
    SELECT id, nome, email, perfil, token
    FROM usuario
    WHERE token=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*)
    FROM usuario
"""

SQL_EMAIL_EXISTE = """
    SELECT COUNT(*)
    FROM usuario
    WHERE email=?
"""
