# -*- coding: utf-8 -*-
"""Gerador de Senhas Seguras com Interface Gráfica (Tkinter) - v2"""

import tkinter as tk
from tkinter import ttk  # For themed widgets
from tkinter import messagebox
import random
import string

# --- Lógica de Geração de Senha (Reutilizada/Adaptada) ---
def gerar_senha_logica(comprimento, usar_minusculas, usar_maiusculas, usar_digitos, usar_simbolos):
    """Gera uma senha aleatória com base nas configurações fornecidas."""
    caracteres = ""
    senha_parcial = []

    # Adiciona os conjuntos de caracteres selecionados e garante pelo menos um de cada
    if usar_minusculas:
        caracteres += string.ascii_lowercase
        senha_parcial.append(random.choice(string.ascii_lowercase))
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
        senha_parcial.append(random.choice(string.ascii_uppercase))
    if usar_digitos:
        caracteres += string.digits
        senha_parcial.append(random.choice(string.digits))
    if usar_simbolos:
        # Escapar caracteres especiais que podem causar problemas em algumas strings ou comandos
        simbolos_seguros = string.punctuation.replace('"', '').replace("\\\'", '').replace('`', '')
        caracteres += simbolos_seguros
        if simbolos_seguros: # Garante que há símbolos seguros para escolher
             senha_parcial.append(random.choice(simbolos_seguros))

    if not caracteres:
        # Isso não deve acontecer se a validação da GUI funcionar
        return None

    # Calcula quantos caracteres restantes são necessários
    comprimento_restante = comprimento - len(senha_parcial)

    # Se o comprimento for menor que os tipos selecionados, pega uma amostra
    if comprimento_restante < 0:
        senha_parcial = random.sample(senha_parcial, k=comprimento)
        comprimento_restante = 0

    # Preenche o restante da senha com caracteres aleatórios dos conjuntos selecionados
    for _ in range(comprimento_restante):
        senha_parcial.append(random.choice(caracteres))

    # Embaralha a senha final para garantir aleatoriedade na posição dos caracteres garantidos
    random.shuffle(senha_parcial)
    senha_gerada = ''.join(senha_parcial)

    return senha_gerada

# --- Funções da Interface --- 
def gerar_e_exibir_senha():
    """Obtém configurações da GUI, gera a senha e a exibe."""
    try:
        comprimento = int(comprimento_var.get())
        if not (8 <= comprimento <= 64):
            messagebox.showerror("Erro de Comprimento", "O comprimento da senha deve estar entre 8 e 64 caracteres.")
            return
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite um número inteiro válido para o comprimento.")
        return

    usar_minusculas = minusculas_var.get()
    usar_maiusculas = maiusculas_var.get()
    usar_digitos = digitos_var.get()
    usar_simbolos = simbolos_var.get()

    if not (usar_minusculas or usar_maiusculas or usar_digitos or usar_simbolos):
        messagebox.showerror("Erro de Seleção", "Selecione pelo menos um tipo de caractere para incluir na senha.")
        return

    senha = gerar_senha_logica(comprimento, usar_minusculas, usar_maiusculas, usar_digitos, usar_simbolos)

    if senha:
        senha_var.set(senha)
    else:
        # Caso a lógica de geração falhe (improvável com validação)
        messagebox.showerror("Erro Interno", "Ocorreu um erro inesperado ao gerar a senha.")
        senha_var.set("")

def copiar_senha():
    """Copia a senha gerada, mostra pop-up e muda texto do botão temporariamente."""
    senha_gerada = senha_var.get()
    if senha_gerada:
        # Copia para a área de transferência
        root.clipboard_clear()
        root.clipboard_append(senha_gerada)

        # Guarda o texto original e muda o botão
        original_text = copiar_button.cget("text")
        copiar_button.config(text="Copiado!", state="disabled")

        # Função para reverter o botão ao estado original
        def revert_button():
            copiar_button.config(text=original_text, state="normal")

        # Agenda a reversão após 2000ms (2 segundos)
        root.after(2000, revert_button)

        # Mostra a janela pop-up de confirmação (conforme solicitado)
        messagebox.showinfo("Copiado", "Senha copiada com sucesso para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Não há senha gerada para copiar.")

# --- Configuração da Janela Principal --- 
root = tk.Tk()
root.title("Gerador de Senhas Seguras")
root.geometry("420x420") # Altura aumentada para garantir visibilidade
root.resizable(False, False) # Impede redimensionamento

# Estilo ttk para uma aparência mais moderna
style = ttk.Style()
# Tenta usar um tema mais moderno se disponível (pode variar por OS)
try:
    # Prioriza temas que permitem colorir botões mais facilmente
    if 'clam' in style.theme_names():
        style.theme_use('clam')
    elif 'alt' in style.theme_names():
        style.theme_use('alt')
    elif 'default' in style.theme_names():
        style.theme_use('default')
    else:
        # Fallback para o primeiro tema disponível se nenhum dos preferidos for encontrado
        style.theme_use(style.theme_names()[0])
except tk.TclError:
     # Em caso de erro ao definir tema, usa o padrão do sistema
     pass

# --- Widgets da Interface --- 

# Frame principal para melhor organização e padding
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill="both")

# Seção de Comprimento
comprimento_frame = ttk.Frame(main_frame)
comprimento_frame.pack(fill="x", pady=5)
ttk.Label(comprimento_frame, text="Comprimento (8-64):").pack(side="left", padx=(0, 10))
comprimento_var = tk.StringVar(value="16") # Padrão aumentado
comprimento_entry = ttk.Entry(comprimento_frame, textvariable=comprimento_var, width=5, justify='center')
comprimento_entry.pack(side="left")

# Seção de Checkboxes para Tipos de Caracteres
checkbox_frame = ttk.LabelFrame(main_frame, text="Incluir Tipos de Caracteres", padding="15")
checkbox_frame.pack(fill="x", pady=10)

minusculas_var = tk.BooleanVar(value=True)
chk_minusculas = ttk.Checkbutton(checkbox_frame, text="Letras Minúsculas (a-z)", variable=minusculas_var)
chk_minusculas.pack(anchor="w", pady=2)

maiusculas_var = tk.BooleanVar(value=True)
chk_maiusculas = ttk.Checkbutton(checkbox_frame, text="Letras Maiúsculas (A-Z)", variable=maiusculas_var)
chk_maiusculas.pack(anchor="w", pady=2)

digitos_var = tk.BooleanVar(value=True)
chk_digitos = ttk.Checkbutton(checkbox_frame, text="Dígitos Numéricos (0-9)", variable=digitos_var)
chk_digitos.pack(anchor="w", pady=2)

simbolos_var = tk.BooleanVar(value=True)
chk_simbolos = ttk.Checkbutton(checkbox_frame, text="Símbolos Especiais (!@#...)", variable=simbolos_var)
chk_simbolos.pack(anchor="w", pady=2)

# Botão para Gerar a Senha
gerar_button = ttk.Button(main_frame, text="🔑 Gerar Senha Segura", command=gerar_e_exibir_senha, style='Accent.TButton') # Estilo opcional
gerar_button.pack(pady=15, ipady=5) # Aumenta o padding vertical interno

# Seção para Exibir a Senha Gerada
senhagerada_frame = ttk.Frame(main_frame)
senhagerada_frame.pack(fill="x", pady=5)
ttk.Label(senhagerada_frame, text="Senha Gerada:").pack(side="left", padx=(0, 10))
senha_var = tk.StringVar()
senha_entry = ttk.Entry(senhagerada_frame, textvariable=senha_var, state="readonly", font=('Courier', 10)) # Fonte monoespaçada
senha_entry.pack(side="left", expand=True, fill="x", ipady=3)

# Configuração de estilo para o botão de copiar (azul)
# Nota: A capacidade de definir cores de fundo pode depender do tema ttk ativo.
# 'clam', 'alt', 'default' geralmente permitem isso melhor que 'vista' ou 'aqua'.
style.configure('Copy.TButton', background='#007bff', foreground='white', font=('Segoe UI', 10))
style.map('Copy.TButton',
    foreground=[('disabled', '#a0a0a0'), ('active', 'white')],
    background=[('disabled', '#cccccc'), ('active', '#0056b3'), ('!disabled', '#007bff')]) # Garante a cor azul no estado normal

# Botão para Copiar a Senha (com novo estilo)
copiar_button = ttk.Button(main_frame, text="📋 Copiar Senha", command=copiar_senha, style='Copy.TButton')
copiar_button.pack(pady=10)

# Configuração de estilo para o botão de gerar (opcional, pode ser ajustado)
style.configure('Accent.TButton', font=('Segoe UI', 10, 'bold'))

# --- Iniciar Loop Principal da Interface --- 
root.mainloop()

