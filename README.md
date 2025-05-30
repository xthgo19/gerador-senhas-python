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
    - O **comprimento** exato da senha (padrão 8-64 caracteres).
    - A inclusão de **letras minúsculas** (`a-z`).
    - A inclusão de **letras maiúsculas** (`A-Z`).
    - A inclusão de **dígitos** (`0-9`).
    - A inclusão de **símbolos** (ex: `!@#$%^&*()`).
- 🖥️ **Interface Dupla:** Oferece tanto uma interface CLI interativa quanto uma GUI amigável com Tkinter.
- ✔️ **Validação de Entrada:** Garante que as configurações fornecidas pelo usuário sejam válidas.
- 📋 **Copiar para Área de Transferência:** Funcionalidade na GUI para copiar a senha gerada com um clique.
- 📦 **Sem Dependências Externas:** Funciona com uma instalação padrão do Python 3 (Tkinter geralmente incluído).

## 🚀 Como Utilizar

### Pré-requisitos
- Python 3.x instalado em seu sistema.

### Execução (Interface Gráfica - GUI)

1.  **Salve o Script:** Certifique-se de ter o arquivo `gerador_senhas_gui_v2.py`.
2.  **Abra o Terminal:** Navegue até o diretório onde salvou o arquivo.
3.  **Execute:** Utilize o comando abaixo:

    ```bash
    python gerador_senhas_gui_v2.py
    ```
    *(ou `python3 gerador_senhas_gui_v2.py` / `py gerador_senhas_gui_v2.py` dependendo da sua configuração)*

4.  **Use a Interface:** Configure as opções na janela e clique em "Gerar Senha Segura". Use o botão "Copiar Senha" para copiar o resultado.

### Execução (Linha de Comando - CLI)

1.  **Salve o Script:** Certifique-se de ter o arquivo `gerador_senhas.py`.
2.  **Abra o Terminal:** Navegue até o diretório onde salvou o arquivo.
3.  **Execute:** Utilize o comando abaixo:

    ```bash
    python gerador_senhas.py
    ```
    *(ou `python3 gerador_senhas.py` / `py gerador_senhas.py` dependendo da sua configuração)*

4.  **Siga as Instruções:** Responda às perguntas no terminal para configurar sua senha.

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem principal do projeto.
- **Módulos Padrão**: `random`, `string`, `sys`.
- **Tkinter**: Para a interface gráfica (geralmente incluído no Python).

## 🔍 Estrutura do Código

```
/gerador-senhas-python
│
├── gerador_senhas.py           # Versão CLI (Linha de Comando)
├── gerador_senhas_gui_v2.py    # Versão GUI (Interface Gráfica)
└── README.md                   # Documentação do projeto
```

## 📈 Futuras Implementações

- [ ] Opção para evitar caracteres ambíguos (ex: `I`, `l`, `1`, `O`, `0`).
- [ ] Capacidade de gerar múltiplas senhas de uma vez (CLI e GUI).
- [ ] Salvar configurações preferidas do usuário (GUI).
- [ ] Empacotar como um executável independente.

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


