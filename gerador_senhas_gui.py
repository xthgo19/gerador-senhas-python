# -*- coding: utf-8 -*-
"""Gerador de Senhas Seguras com Interface Gráfica (Tkinter) - v5 (Salva Configs)"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import random
import string
import json # Para salvar/carregar configurações
import os   # Para obter o diretório do script

# --- Constantes ---
CONFIG_FILE = "gerador_senhas_config.json"

# --- Lógica de Geração de Senha (Mesma da v4) ---
def gerar_senha_logica(comprimento, usar_minusculas, usar_maiusculas, usar_digitos, usar_simbolos, evitar_ambiguos):
    """Gera UMA senha aleatória com base nas configurações fornecidas."""
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

# --- Funções da Interface (Modificada) --- 
def gerar_e_exibir_senhas():
    """Obtém configurações da GUI, gera a(s) senha(s) e a(s) exibe."""
    try:
        quantidade = int(quantidade_var.get())
        if not (1 <= quantidade <= 100):
            messagebox.showerror("Erro de Quantidade", "A quantidade de senhas deve estar entre 1 e 100.")
            return
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite um número inteiro válido para a quantidade.")
        return
        
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
    evitar_ambiguos = ambiguos_var.get()

    if not (usar_minusculas or usar_maiusculas or usar_digitos or usar_simbolos):
        messagebox.showerror("Erro de Seleção", "Selecione pelo menos um tipo de caractere para incluir na senha.")
        return

    senhas_geradas_lista = []
    falhas = 0
    for _ in range(quantidade):
        senha = gerar_senha_logica(comprimento, usar_minusculas, usar_maiusculas, usar_digitos, usar_simbolos, evitar_ambiguos)
        if senha:
            senhas_geradas_lista.append(senha)
        else:
            falhas += 1

    senhas_text.config(state='normal')
    senhas_text.delete('1.0', tk.END)
    
    if senhas_geradas_lista:
        senhas_formatadas = "\n".join(senhas_geradas_lista)
        senhas_text.insert(tk.END, senhas_formatadas)
    else:
        senhas_text.insert(tk.END, "Nenhuma senha gerada.")
        
    senhas_text.config(state='disabled')

    if falhas > 0:
        messagebox.showwarning("Aviso de Falha", f"{falhas} senha(s) não puderam ser geradas devido à combinação de opções.")

def copiar_senhas():
    """Copia TODAS as senhas geradas."""
    senhas_geradas_texto = senhas_text.get('1.0', tk.END).strip()
    
    if senhas_geradas_texto and senhas_geradas_texto != "Nenhuma senha gerada.":
        root.clipboard_clear()
        root.clipboard_append(senhas_geradas_texto)
        
        original_text = copiar_button.cget("text")
        copiar_button.config(text="Copiado!", state="disabled")
        def revert_button():
            copiar_button.config(text=original_text, state="normal")
        root.after(2000, revert_button)
        
        messagebox.showinfo("Copiado", f"{len(senhas_geradas_texto.splitlines())} senha(s) copiada(s) com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Não há senhas geradas para copiar.")

# --- Funções de Configuração --- 
def get_script_dir():
    """Retorna o diretório onde o script está sendo executado."""
    # Se executando como script normal
    if "__file__" in globals():
        return os.path.dirname(os.path.abspath(__file__))
    # Se executando de forma interativa ou empacotado (fallback)
    return os.getcwd()

def load_config():
    """Carrega as configurações do arquivo JSON, se existir."""
    config_path = os.path.join(get_script_dir(), CONFIG_FILE)
    try:
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                # Define os valores das variáveis Tkinter com base no config
                quantidade_var.set(config.get('quantidade', '1'))
                comprimento_var.set(config.get('comprimento', '16'))
                minusculas_var.set(config.get('usar_minusculas', True))
                maiusculas_var.set(config.get('usar_maiusculas', True))
                digitos_var.set(config.get('usar_digitos', True))
                simbolos_var.set(config.get('usar_simbolos', True))
                ambiguos_var.set(config.get('evitar_ambiguos', False))
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar configurações de {config_path}: {e}")
        # Usa padrões se o carregamento falhar
        set_default_configs()

def save_config():
    """Salva as configurações atuais no arquivo JSON."""
    config = {
        'quantidade': quantidade_var.get(),
        'comprimento': comprimento_var.get(),
        'usar_minusculas': minusculas_var.get(),
        'usar_maiusculas': maiusculas_var.get(),
        'usar_digitos': digitos_var.get(),
        'usar_simbolos': simbolos_var.get(),
        'evitar_ambiguos': ambiguos_var.get()
    }
    config_path = os.path.join(get_script_dir(), CONFIG_FILE)
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Erro ao salvar configurações em {config_path}: {e}")

def set_default_configs():
    """Define os valores padrão para as variáveis Tkinter."""
    quantidade_var.set('1')
    comprimento_var.set('16')
    minusculas_var.set(True)
    maiusculas_var.set(True)
    digitos_var.set(True)
    simbolos_var.set(True)
    ambiguos_var.set(False)

def on_closing():
    """Função chamada quando a janela é fechada."""
    save_config() # Salva as configurações antes de fechar
    root.destroy()

# --- Configuração da Janela Principal --- 
root = tk.Tk()
root.title("Gerador de Senhas Seguras")
root.geometry("450x550") 
root.resizable(False, False) 

style = ttk.Style()
try:
    if 'clam' in style.theme_names():
        style.theme_use('clam')
    elif 'alt' in style.theme_names():
        style.theme_use('alt')
    elif 'default' in style.theme_names():
        style.theme_use('default')
    else:
        style.theme_use(style.theme_names()[0])
except tk.TclError:
     pass

# --- Variáveis Tkinter --- (Definidas antes de carregar config)
quantidade_var = tk.StringVar()
comprimento_var = tk.StringVar()
minusculas_var = tk.BooleanVar()
maiusculas_var = tk.BooleanVar()
digitos_var = tk.BooleanVar()
simbolos_var = tk.BooleanVar()
ambiguos_var = tk.BooleanVar()

# --- Carregar Configurações ou Definir Padrões ---
load_config() # Tenta carregar configs salvas

# --- Widgets da Interface --- 

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill="both")

config_frame = ttk.Frame(main_frame)
config_frame.pack(fill="x", pady=5)

quantidade_frame = ttk.Frame(config_frame)
quantidade_frame.pack(side="left", padx=(0, 20))
ttk.Label(quantidade_frame, text="Quantidade (1-100):").pack(anchor='w')
quantidade_entry = ttk.Entry(quantidade_frame, textvariable=quantidade_var, width=5, justify='center')
quantidade_entry.pack(anchor='w')

comprimento_frame = ttk.Frame(config_frame)
comprimento_frame.pack(side="left")
ttk.Label(comprimento_frame, text="Comprimento (8-64):").pack(anchor='w')
comprimento_entry = ttk.Entry(comprimento_frame, textvariable=comprimento_var, width=5, justify='center')
comprimento_entry.pack(anchor='w')

checkbox_frame = ttk.LabelFrame(main_frame, text="Opções de Caracteres", padding="15")
checkbox_frame.pack(fill="x", pady=10)

chk_minusculas = ttk.Checkbutton(checkbox_frame, text="Letras Minúsculas (a-z)", variable=minusculas_var)
chk_minusculas.pack(anchor="w", pady=2)

chk_maiusculas = ttk.Checkbutton(checkbox_frame, text="Letras Maiúsculas (A-Z)", variable=maiusculas_var)
chk_maiusculas.pack(anchor="w", pady=2)

chk_digitos = ttk.Checkbutton(checkbox_frame, text="Dígitos Numéricos (0-9)", variable=digitos_var)
chk_digitos.pack(anchor="w", pady=2)

chk_simbolos = ttk.Checkbutton(checkbox_frame, text="Símbolos Especiais (!@#...)", variable=simbolos_var)
chk_simbolos.pack(anchor="w", pady=2)

chk_ambiguos = ttk.Checkbutton(checkbox_frame, text="Evitar Caracteres Ambíguos (I, l, 1, O, 0)", variable=ambiguos_var)
chk_ambiguos.pack(anchor="w", pady=2)

gerar_button = ttk.Button(main_frame, text="🔑 Gerar Senha(s)", command=gerar_e_exibir_senhas, style='Accent.TButton')
gerar_button.pack(pady=15, ipady=5)

ttk.Label(main_frame, text="Senha(s) Gerada(s):").pack(anchor='w', pady=(5,2))
senhas_text = scrolledtext.ScrolledText(main_frame, height=6, width=50, wrap=tk.WORD, state='disabled', font=('Courier', 10))
senhas_text.pack(fill="x", expand=True, pady=(0, 10))

style.configure('Copy.TButton', background='#007bff', foreground='white', font=('Segoe UI', 10))
style.map('Copy.TButton',
    foreground=[('disabled', '#a0a0a0'), ('active', 'white')],
    background=[('disabled', '#cccccc'), ('active', '#0056b3'), ('!disabled', '#007bff')])
style.configure('Accent.TButton', font=('Segoe UI', 10, 'bold'))

copiar_button = ttk.Button(main_frame, text="📋 Copiar Senha(s)", command=copiar_senhas, style='Copy.TButton')
copiar_button.pack(pady=5)

# --- Vincula o fechamento da janela à função on_closing --- 
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

