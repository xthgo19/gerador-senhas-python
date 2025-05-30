# 🔐 Gerador de Senhas Seguras em Python

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version Badge"/>
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status Badge"/>
  <img src="https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge" alt="License Badge"/>
</div>

## 📋 Sobre o Projeto

Um script Python robusto e interativo para a geração de senhas aleatórias e seguras. Idealizado para fortalecer a segurança digital do usuário de forma simples e eficaz, este projeto utiliza a linha de comando (CLI) para uma experiência direta e personalizável.

## ✨ Funcionalidades Principais

- 🔑 **Geração Aleatória:** Cria senhas utilizando os módulos `random` e `string` do Python para garantir alta entropia.
- ⚙️ **Personalização Completa:** Permite ao usuário definir:
    - O **comprimento** exato da senha (padrão 8-64 caracteres).
    - A inclusão de **letras minúsculas** (`a-z`).
    - A inclusão de **letras maiúsculas** (`A-Z`).
    - A inclusão de **dígitos** (`0-9`).
    - A inclusão de **símbolos** (ex: `!@#$%^&*()`).
- 🖥️ **Interface CLI Intuitiva:** Guias interativas para facilitar a configuração da senha desejada.
- ✔️ **Validação de Entrada:** Garante que as configurações fornecidas pelo usuário sejam válidas.
- 📦 **Sem Dependências Externas:** Funciona com uma instalação padrão do Python 3.

## 🚀 Como Utilizar

### Pré-requisitos
- Python 3.x instalado em seu sistema.

### Execução

1.  **Salve o Script:** Faça o download ou copie o código para um arquivo chamado `gerador_senhas.py`.
2.  **Abra o Terminal:** Navegue até o diretório onde salvou o arquivo.
3.  **Execute:** Utilize o comando abaixo:

    ```bash
    python gerador_senhas.py
    ```
    *(ou `python3 gerador_senhas.py` / `py gerador_senhas.py` dependendo da sua configuração)*

4.  **Siga as Instruções:** Responda às perguntas para configurar sua senha.

### Demonstração de Uso

```
--- Configuração da Senha ---
Digite o comprimento da senha [8-64] (padrão: 12): 16
Incluir letras minúsculas (a-z)? (s/n, padrão: s): s
Incluir letras maiúsculas (A-Z)? (s/n, padrão: s): s
Incluir dígitos (0-9)? (s/n, padrão: s): s
Incluir símbolos (!@#$%^&*()_+-=[]{};':"\|,.<>/?`)? (s/n, padrão: s): n

--- Senha Gerada ---
4kR7pW9jL1mX3sQ8
--------------------
```

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem principal do projeto.
- **Módulos Padrão**: `random`, `string`, `sys`.

## 🔍 Estrutura do Código (`gerador_senhas.py`)

O script é organizado em funções para clareza e manutenção:

- **`obter_configuracoes()`**: Responsável pela interação com o usuário e coleta das preferências.
- **`gerar_senha(...)`**: Contém a lógica principal para a geração da senha aleatória com base nas configurações.
- **Bloco `if __name__ == "__main__":`**: Ponto de entrada que orquestra a execução das funções.

## 📈 Futuras Implementações

- [ ] Opção para evitar caracteres ambíguos (ex: `I`, `l`, `1`, `O`, `0`).
- [ ] Capacidade de gerar múltiplas senhas de uma vez.
- [ ] Opção para copiar a senha gerada diretamente para a área de transferência.
- [ ] Interface gráfica (GUI) utilizando Tkinter ou outra biblioteca.
- [ ] Salvar configurações preferidas do usuário.

## 👨‍💻 Autor

<div align="center">
  <!-- Substitua com a imagem e informações do autor real -->
  <img src="https://via.placeholder.com/100" width="100px" style="border-radius: 50%" alt="Foto do Autor"/>
  <br/>
  <strong>[Seu Nome ou Nickname]</strong>
  <br/>
  <a href="[Link para seu GitHub]">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Badge"/>
  </a>
  <a href="[Link para seu LinkedIn]">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</div>

## 📄 Licença

Este projeto está distribuído sob a licença MIT. Veja o arquivo `LICENSE` (se existir) para mais detalhes.

---

<div align="center">
  <p>⭐ Se este projeto foi útil, considere dar uma estrela no repositório! ⭐</p>
  <p>Desenvolvido com Python 🐍</p>
</div>

