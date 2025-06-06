# -*- coding: utf-8 -*-
"""Gerador de Senhas Seguras - v3 (Múltiplas Senhas)

Este script gera uma ou mais senhas aleatórias e seguras com base nas
preferências do usuário, como comprimento, tipos de caracteres, opção para
evitar caracteres ambíguos e quantidade. Utiliza uma interface de linha
de comando interativa.
"""

import random
import string
import sys

def obter_configuracoes():
    """Coleta as configurações do usuário para a geração da(s) senha(s).

    Solicita interativamente o comprimento, tipos de caracteres, se evita
    ambíguos e a quantidade de senhas a gerar.

    Returns:
        tuple: Uma tupla contendo:
            - quantidade (int): Número de senhas a gerar.
            - comprimento (int): O comprimento de cada senha.
            - usar_minusculas (bool): True se letras minúsculas devem ser incluídas.
            - usar_maiusculas (bool): True se letras maiúsculas devem ser incluídas.
            - usar_digitos (bool): True se dígitos devem ser incluídos.
            - usar_simbolos (bool): True se símbolos devem ser incluídos.
            - evitar_ambiguos (bool): True se caracteres ambíguos devem ser evitados.
    """
    print("--- Configuração da(s) Senha(s) ---")

    # Obter quantidade de senhas
    quantidade_padrao = 1
    quantidade_max = 100 # Limite razoável
    while True:
        try:
            entrada_quantidade = input(f"Quantas senhas deseja gerar [1-{quantidade_max}] (padrão: {quantidade_padrao}): ")
            if not entrada_quantidade:
                quantidade = quantidade_padrao
                print(f"Gerando {quantidade} senha.")
                break
            quantidade = int(entrada_quantidade)
            if 1 <= quantidade <= quantidade_max:
                break
            else:
                print(f"Erro: A quantidade deve estar entre 1 e {quantidade_max}.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")
        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada/interrompida pelo usuário.")
            sys.exit(0)

    # Obter comprimento da senha
    comprimento_padrao = 16
    comprimento_min = 8
    comprimento_max = 64
    while True:
        try:
            entrada_comprimento = input(f"Digite o comprimento de cada senha [{comprimento_min}-{comprimento_max}] (padrão: {comprimento_padrao}): ")
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
            simbolos_exemplo = string.punctuation.replace('"', '').replace("\\'", '').replace('`', '')
            usar_simbolos = input(f"Incluir símbolos (ex: {simbolos_exemplo[:10]}...)? (s/n, padrão: s): ").lower() != 'n'
            evitar_ambiguos = input("Evitar caracteres ambíguos (I, l, 1, O, 0)? (s/n, padrão: n): ").lower() == 's'

            if not (usar_minusculas or usar_maiusculas or usar_digitos or usar_simbolos):
                print("Erro: Pelo menos um tipo de caractere deve ser selecionado.")
            else:
                break
        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada/interrompida pelo usuário.")
            sys.exit(0)

    return quantidade, comprimento, usar_minusculas, usar_maiusculas, usar_digitos, usar_simbolos, evitar_ambiguos

def gerar_senha(comprimento, usar_minusculas, usar_maiusculas, usar_digitos, usar_simbolos, evitar_ambiguos):
    """Gera UMA senha aleatória com base nas configurações fornecidas.
       (Mesma lógica da v2)
    """
    ambiguos = 'Il1O0'
    conjunto_minusculas = string.ascii_lowercase
    conjunto_maiusculas = string.ascii_uppercase
    conjunto_digitos = string.digits
    conjunto_simbolos = string.punctuation.replace('"', '').replace("\\'", '').replace('`', '')

    if evitar_ambiguos:
        conjunto_minusculas = ''.join(c for c in conjunto_minusculas if c not in ambiguos)
        conjunto_maiusculas = ''.join(c for c in conjunto_maiusculas if c not in ambiguos)
        conjunto_digitos = ''.join(c for c in conjunto_digitos if c not in ambiguos)

    caracteres_disponiveis = ""
    senha_parcial = []

    if usar_minusculas and conjunto_minusculas:
        caracteres_disponiveis += conjunto_minusculas
        senha_parcial.append(random.choice(conjunto_minusculas))
    if usar_maiusculas and conjunto_maiusculas:
        caracteres_disponiveis += conjunto_maiusculas
        senha_parcial.append(random.choice(conjunto_maiusculas))
    if usar_digitos and conjunto_digitos:
        caracteres_disponiveis += conjunto_digitos
        senha_parcial.append(random.choice(conjunto_digitos))
    if usar_simbolos and conjunto_simbolos:
        caracteres_disponiveis += conjunto_simbolos
        senha_parcial.append(random.choice(conjunto_simbolos))

    if not caracteres_disponiveis:
        # Retorna None para indicar falha na geração desta senha específica
        return None

    comprimento_restante = comprimento - len(senha_parcial)

    if comprimento_restante < 0:
        senha_parcial = random.sample([c for c in senha_parcial if c in caracteres_disponiveis], k=comprimento)
        comprimento_restante = 0

    for _ in range(comprimento_restante):
        senha_parcial.append(random.choice(caracteres_disponiveis))

    random.shuffle(senha_parcial)
    senha_gerada = ''.join(senha_parcial)

    return senha_gerada

if __name__ == "__main__":
    try:
        # Obtém todas as configurações, incluindo a quantidade
        qtd, comp, minusc, maiusc, digit, simb, ambig = obter_configuracoes()
        
        senhas_geradas = []
        falhas = 0
        print("\nGerando senhas...")
        for i in range(qtd):
            senha = gerar_senha(comp, minusc, maiusc, digit, simb, ambig)
            if senha:
                senhas_geradas.append(senha)
            else:
                # Se gerar_senha retornar None, registra a falha
                falhas += 1
                print(f"Aviso: Falha ao gerar a senha #{i+1} com as opções selecionadas.")
                print("(Verifique se todos os caracteres dos tipos escolhidos não são ambíguos quando essa opção está ativa).")

        if senhas_geradas:
            print(f"\n--- {len(senhas_geradas)} Senha(s) Gerada(s) ---")
            for idx, s in enumerate(senhas_geradas):
                print(f"{idx+1}: {s}")
            print("-------------------------")
        
        if falhas > 0:
             print(f"\n{falhas} senha(s) não puderam ser geradas devido à combinação de opções.")

    except SystemExit:
        pass # Usuário cancelou
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

