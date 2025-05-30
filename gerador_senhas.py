# -*- coding: utf-8 -*-
"""Gerador de Senhas Seguras

Este script gera senhas aleatórias e seguras com base nas preferências
do usuário, como comprimento e tipos de caracteres a serem incluídos.
Utiliza uma interface de linha de comando interativa.
"""

import random
import string
import sys

def obter_configuracoes():
    """Coleta as configurações do usuário para a geração da senha.

    Solicita interativamente o comprimento desejado e quais conjuntos de
    caracteres (minúsculas, maiúsculas, dígitos, símbolos) devem ser
    incluídos na senha. Realiza validações básicas nas entradas.

    Returns:
        tuple: Uma tupla contendo:
            - comprimento (int): O comprimento da senha.
            - usar_minusculas (bool): True se letras minúsculas devem ser incluídas.
            - usar_maiusculas (bool): True se letras maiúsculas devem ser incluídas.
            - usar_digitos (bool): True se dígitos devem ser incluídos.
            - usar_simbolos (bool): True se símbolos devem ser incluídos.
    """
    print("--- Configuração da Senha ---")

    # Obter comprimento da senha
    comprimento_padrao = 12
    comprimento_min = 8
    comprimento_max = 64
    while True:
        try:
            entrada_comprimento = input(f"Digite o comprimento da senha [{comprimento_min}-{comprimento_max}] (padrão: {comprimento_padrao}): ")
            if not entrada_comprimento:
                comprimento = comprimento_padrao
                print(f"Usando comprimento padrão: {comprimento}")
                break
            comprimento = int(entrada_comprimento)
            if comprimento_min <= comprimento <= comprimento_max:
                break
            else:
                print(f"Erro: O comprimento deve estar entre {comprimento_min} e {comprimento_max}.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")
        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada/interrompida pelo usuário.")
            sys.exit(0)

    # Obter tipos de caracteres
    while True:
        try:
            usar_minusculas = input("Incluir letras minúsculas (a-z)? (s/n, padrão: s): ").lower() != 'n'
            usar_maiusculas = input("Incluir letras maiúsculas (A-Z)? (s/n, padrão: s): ").lower() != 'n'
            usar_digitos = input("Incluir dígitos (0-9)? (s/n, padrão: s): ").lower() != 'n'
            usar_simbolos = input(f"Incluir símbolos ({string.punctuation})? (s/n, padrão: s): ").lower() != 'n'

            if not (usar_minusculas or usar_maiusculas or usar_digitos or usar_simbolos):
                print("Erro: Pelo menos um tipo de caractere deve ser selecionado.")
            else:
                break
        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada/interrompida pelo usuário.")
            sys.exit(0)

    return comprimento, usar_minusculas, usar_maiusculas, usar_digitos, usar_simbolos

def gerar_senha(comprimento, usar_minusculas, usar_maiusculas, usar_digitos, usar_simbolos):
    """Gera uma senha aleatória com base nas configurações fornecidas.

    Args:
        comprimento (int): O comprimento da senha.
        usar_minusculas (bool): Incluir letras minúsculas.
        usar_maiusculas (bool): Incluir letras maiúsculas.
        usar_digitos (bool): Incluir dígitos.
        usar_simbolos (bool): Incluir símbolos.

    Returns:
        str: A senha gerada aleatoriamente.
    """
    caracteres = ""
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        print("Erro interno: Nenhum conjunto de caracteres disponível.")
        return None

    # Linha corrigida:
    senha_gerada = ''.join(random.choices(caracteres, k=comprimento))

    return senha_gerada

if __name__ == "__main__":
    try:
        comprimento, minusculas, maiusculas, digitos, simbolos = obter_configuracoes()
        senha = gerar_senha(comprimento, minusculas, maiusculas, digitos, simbolos)

        if senha:
            print("\n--- Senha Gerada ---")
            print(senha)
            print("--------------------")

    except SystemExit:
        pass
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

