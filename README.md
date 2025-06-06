# 🔐 Gerador de Senhas Seguras em Python

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version Badge"/>
  <img src="https://img.shields.io/badge/Interface-CLI%20%26%20GUI%20(Tkinter)-blueviolet?style=for-the-badge" alt="Interface Badge"/>
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status Badge"/>
  <img src="https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge" alt="License Badge"/>
</div>

## 📋 Sobre o Projeto

Um script Python robusto e interativo para a geração de senhas aleatórias e seguras. Idealizado para fortalecer a segurança digital do usuário de forma simples e eficaz, este projeto oferece tanto uma interface de linha de comando (CLI) quanto uma interface gráfica (GUI com Tkinter) para uma experiência direta e personalizável.

## ✨ Funcionalidades Principais

- 🔑 **Geração Aleatória:** Cria senhas utilizando os módulos `random` e `string` do Python para garantir alta entropia.
- ⚙️ **Personalização Completa:** Permite ao usuário definir:
    - A **quantidade** de senhas a serem geradas (1-100).
    - O **comprimento** exato de cada senha (padrão 8-64 caracteres).
    - A inclusão de **letras minúsculas** (`a-z`).
    - A inclusão de **letras maiúsculas** (`A-Z`).
    - A inclusão de **dígitos** (`0-9`).
    - A inclusão de **símbolos** (ex: `!@#$%^&*()`).
    - A opção de **evitar caracteres ambíguos** (como `I`, `l`, `1`, `O`, `0`).
- 🖥️ **Interface Dupla:** Oferece tanto uma interface CLI interativa quanto uma GUI amigável com Tkinter.
- 💾 **Salvar Preferências (GUI):** A versão gráfica salva automaticamente as últimas configurações utilizadas em um arquivo `gerador_senhas_config.json` para conveniência.
- ✔️ **Validação de Entrada:** Garante que as configurações fornecidas pelo usuário sejam válidas.
- 📋 **Copiar para Área de Transferência:** Funcionalidade na GUI para copiar a(s) senha(s) gerada(s) com um clique.
- 📦 **Empacotável:** Pode ser facilmente transformado em um executável independente usando PyInstaller.

## 🚀 Como Utilizar

### Pré-requisitos
- Python 3.x instalado em seu sistema.

### Execução (Interface Gráfica - GUI)

1.  **Salve o Script:** Certifique-se de ter o arquivo `gerador_senhas_gui_v5.py`.
2.  **Abra o Terminal:** Navegue até o diretório onde salvou o arquivo.
3.  **Execute:** Utilize o comando abaixo:

    ```bash
    python gerador_senhas_gui_v5.py
    ```
    *(ou `python3 gerador_senhas_gui_v5.py` / `py gerador_senhas_gui_v5.py` dependendo da sua configuração)*

4.  **Use a Interface:** Configure a quantidade, comprimento e as opções de caracteres na janela. Clique em "Gerar Senha(s)". Use o botão "Copiar Senha(s)" para copiar os resultados. As configurações serão salvas automaticamente ao fechar.

### Execução (Linha de Comando - CLI)

1.  **Salve o Script:** Certifique-se de ter o arquivo `gerador_senhas_v3.py`.
2.  **Abra o Terminal:** Navegue até o diretório onde salvou o arquivo.
3.  **Execute:** Utilize o comando abaixo:

    ```bash
    python gerador_senhas_v3.py
    ```
    *(ou `python3 gerador_senhas_v3.py` / `py gerador_senhas_v3.py` dependendo da sua configuração)*

4.  **Siga as Instruções:** Responda às perguntas no terminal para configurar a quantidade, comprimento e tipos de caracteres para suas senhas.

## 📦 Criando um Executável Independente (Opcional)

Você pode empacotar este projeto para rodar em computadores Windows sem precisar instalar o Python, usando o PyInstaller.

1.  **Instale o PyInstaller:**
    ```bash
    # Tente um destes comandos no seu terminal
    pip install pyinstaller
    python -m pip install pyinstaller
    py -m pip install pyinstaller
    ```
2.  **Navegue até a Pasta do Projeto:**
    ```bash
    cd caminho/para/sua/pasta/gerador-senhas
    ```
3.  **Empacote a GUI:**
    ```bash
    pyinstaller --onefile --windowed --name GeradorSenhasGUI gerador_senhas_gui_v5.py
    ```
4.  **Empacote a CLI:**
    ```bash
    pyinstaller --onefile --name GeradorSenhasCLI gerador_senhas_v3.py
    ```
5.  **Encontre os Executáveis:** Os arquivos `GeradorSenhasGUI.exe` e `GeradorSenhasCLI.exe` estarão na pasta `dist` criada pelo PyInstaller.

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem principal do projeto.
- **Módulos Padrão**: `random`, `string`, `sys`, `json`, `os`.
- **Tkinter**: Para a interface gráfica (geralmente incluído no Python).
- **PyInstaller (Opcional)**: Para empacotamento.

## 🔍 Estrutura do Código

```
/gerador-senhas-python
│
├── gerador_senhas_v3.py           # Versão CLI (Múltiplas Senhas, Evita Ambíguos)
├── gerador_senhas_gui_v5.py     # Versão GUI (Múltiplas Senhas, Evita Ambíguos, Salva Configs)
├── gerador_senhas_config.json   # Arquivo de configuração da GUI (criado automaticamente)
└── README.md                    # Documentação do projeto
```

## 📈 Funcionalidades Implementadas

- [x] Opção para evitar caracteres ambíguos (ex: `I`, `l`, `1`, `O`, `0`).
- [x] Capacidade de gerar múltiplas senhas de uma vez (CLI e GUI).
- [x] Salvar configurações preferidas do usuário (GUI).
- [x] Empacotar como um executável independente (Instruções fornecidas).

## 👨‍💻 Autor

<div align="center">
  <img src="https://avatars.githubusercontent.com/u/149385663?v=4" width="100px" style="border-radius: 50%" alt="Foto de Thiago Pereira"/>
  <br/>
  <strong>Thiago Pereira</strong>
  <br/>
  <a href="https://github.com/xthgo19">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"/>
  </a>
  <a href="https://www.linkedin.com/in/xthgo19">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</div>

## 📄 Licença

Este projeto está distribuído sob a licença MIT. Isso significa que você pode usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do software livremente, desde que o aviso de copyright e esta permissão sejam incluídos em todas as cópias ou partes substanciais do software.

---

<div align="center">
  <p>⭐ Se este projeto foi útil, considere dar uma estrela no repositório! ⭐</p>
  <p>Desenvolvido com Python 🐍 e Tkinter</p>
</div>

