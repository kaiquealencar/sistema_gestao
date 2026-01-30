import re

def validar_cpf_cnpj(value):
    numeros = re.sub(r'\D', '', value)

    if len(numeros) == 11:
        if not validar_cpf(numeros):
            raise ValueError("CPF inválido")
    elif len(numeros) == 14:
        if not validar_cnpj(numeros):
            raise ValueError("CNPJ inválido")
    else:
        raise ValueError("Número de dígitos inválido (CPF = 11, CNPJ = 14)")

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i+1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if int(cpf[i]) != digito:
            return False
    return True

def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calc_digito(cnpj, pos):
        pesos = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        soma = sum(int(cnpj[i]) * pesos[i+pos-1] for i in range(pos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    dig1 = calc_digito(cnpj, 0)
    dig2 = calc_digito(cnpj, 1)
    return int(cnpj[12]) == dig1 and int(cnpj[13]) == dig2
