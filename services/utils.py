def normalizar_telefone(numero):
    numero_telefone = "".join(filter(str.isdigit, numero))
    numero_telefone = "+55" + numero_telefone if not numero_telefone.startswith("55") else numero_telefone

    return numero_telefone

    