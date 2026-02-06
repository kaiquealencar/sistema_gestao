import re
def normalizar_telefone(numero):
    apenas_numeros = re.sub(r'\D', '', str(numero))
    apenas_numeros = apenas_numeros.lstrip('0')

    if not apenas_numeros.startswith("55"):
        apenas_numeros = "55" + apenas_numeros

    return apenas_numeros

    