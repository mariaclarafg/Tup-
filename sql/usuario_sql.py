SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,
    data_nascimento DATE NOT NULL, 
    cpf TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL UNIQUE, 
    senha TEXT NOT NULL,
    perfil INTEGER NOT NULL,
    endereco_cep TEXT,
    endereco_logradouro TEXT,
    endereco_numero TEXT,
    endereco_complemento TEXT,
    endereco_bairro TEXT,
    endereco_cidade TEXT,
    endereco_uf TEXT,
    nome_loja TEXT, 
    cnpj TEXT,
    telefone_loja TEXT,
    tipo_comunidade TEXT
    )
"""

SQL_INSERIR_USUARIO = """
    INSERT INTO usuario 
    (nome, data_nascimento, cpf, cnpj, tipo_comunidade, nome_loja,  email, telefone, senha, perfil)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SQL_CHECAR_CREDENCIAIS = """
    SELECT id, nome, email, perfil, senha
    FROM usuario
    WHERE email = ?
"""

SQL_ATUALIZAR_DADOS_PESSOAIS = """
    UPDATE usuario
    SET nome = ?, data_nascimento=?, cpf=?, email = ?, telefone = ?
    WHERE email = ?
"""

SQL_ATUALIZAR_SENHA = """
    UPDATE usuario
    SET senha = ?
    WHERE email = ?
"""

SQL_ATUALIZAR_TEMA = """
    UPDATE usuario
    SET tema = ?
    WHERE email = ?
"""

SQL_EXCLUIR_USUARIO = """
    DELETE FROM usuario
    WHERE email = ?
"""

SQL_OBTER_POR_ID = """
 SELECT id, nome, data_nascimento, cpf, email, telefone, senha, perfil, endereco_cep, endereco_logradouro, endereco_numero, endereco_complemento, endereco_bairro, endereco_cidade, endereco_uf
    FROM usuario
    WHERE id=?

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


SQL_ATUALIZAR_ENDERECO = """
    UPDATE usuario SET
    endereco_cep=?,
    endereco_logradouro=?,
    endereco_numero=?,
    endereco_complemento=?,
    endereco_bairro=?,
    endereco_cidade=?,
    endereco_uf=?
    WHERE id=?
"""