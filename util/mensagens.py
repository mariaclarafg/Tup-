def adicionar_mensagem(response, mensagem, tipo):
    response.set_cookie(
        key=f"mensagem_{tipo}",
        value=mensagem,
        max_age=3,
        httponly=True,
        samesite="strict",
    )


def adicionar_mensagem_danger(response, mensagem):
    adicionar_mensagem(response, mensagem, "perigo")

def adicionar_mensagem_info(response, mensagem):
    adicionar_mensagem(response, mensagem, "info")

def adicionar_mensagem_sucess(response, mensagem):
    adicionar_mensagem(response, mensagem, "sucesso")

def adicionar_mensagem_warning(response, mensagem):
    adicionar_mensagem(response, mensagem, "warning")
