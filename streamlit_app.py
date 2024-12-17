import re
import streamlit as st

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10) % 11
    if primeiro_digito == 10:
        primeiro_digito = 0

    if int(cpf[9]) != primeiro_digito:
        return False

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10) % 11
    if segundo_digito == 10:
        segundo_digito = 0

    return int(cpf[10]) == segundo_digito

def validar_cnpj(cnpj):
    # Remove caracteres não numéricos
    cnpj = re.sub(r'\D', '', cnpj)

    if len(cnpj) != 14 or cnpj == cnpj[0] * len(cnpj):
        return False

    # Tabelas de multiplicadores
    multiplicador_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicador_2 = [6] + multiplicador_1

    # Calcula o primeiro dígito verificador
    soma = sum(int(cnpj[i]) * multiplicador_1[i] for i in range(12))
    primeiro_digito = soma % 11
    if primeiro_digito < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - primeiro_digito

    if int(cnpj[12]) != primeiro_digito:
        return False

    # Calcula o segundo dígito verificador
    soma = sum(int(cnpj[i]) * multiplicador_2[i] for i in range(13))
    segundo_digito = soma % 11
    if segundo_digito < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - segundo_digito

    return int(cnpj[13]) == segundo_digito

def identificar_e_validar(numero):
    numero = re.sub(r'\D', '', numero)  # Remove caracteres não numéricos

    if len(numero) == 11:
        if validar_cpf(numero):
            return "É um CPF válido."
        else:
            return "É um CPF inválido."
    elif len(numero) == 14:
        if validar_cnpj(numero):
            return "É um CNPJ válido."
        else:
            return "É um CNPJ inválido."
    else:
        return "Número inválido. Não é um CPF nem um CNPJ."

# Aplicação Streamlit
st.title("Validador de CPF e CNPJ")

numero = st.text_input("Digite o CPF ou CNPJ:")

if numero:
    resultado = identificar_e_validar(numero)
    
    st.write(resultado)
