import re
import random
import string

def normalizar_telefone(numero):
    apenas_numeros = re.sub(r'\D', '', str(numero))
    apenas_numeros = apenas_numeros.lstrip('0')

    if not apenas_numeros.startswith("55"):
        apenas_numeros = "55" + apenas_numeros

    return apenas_numeros


def gerar_codigo_produto(model_class, categoria, nome):   

    iniciais_categoria = extrar_iniciais(categoria)
    iniciais_nome = extrar_iniciais(nome)
    codigo = ''.join(random.choices(string.digits, k=4))

    while True:
        novo_codigo = f"{iniciais_categoria}{iniciais_nome}{codigo}"

        if not model_class.objects.filter(codigo=novo_codigo).exists():
            return novo_codigo   


def extrar_iniciais(texto):
    if not texto:
        return "XX"
    
    palavras = [p for p in texto.split() if p]
    inicias = ''.join([p[0] for p in palavras]).upper()
    return inicias if inicias else "XX"


    