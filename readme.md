# Meu Projeto Flask

## O que é

**Meu Projeto Flask** este projeto é um chatbot interativo que permite aos usuários fazer perguntas sobre os dados contidos em um arquivo Excel. Utilizando a API da OpenAI, o chatbot gera respostas baseadas nas informações do arquivo, oferecendo insights e análises em tempo real.

## Funcionalidades

- **Interação com o usuário**: Os usuários podem fazer perguntas sobre o conteúdo do arquivo Excel, como:
  - Quantidade de linhas e colunas.
  - Descrição das colunas.
  - Palavras mais frequentes em colunas específicas.
  - Nomes mais comuns.
  - E muito mais!

- **Interface web**: Uma interface intuitiva onde os usuários podem digitar suas perguntas e receber respostas instantâneas.


## Como foi feito

Esta aplicação foi construída utilizando as seguintes tecnologias:

- **Python 3.x**: Linguagem de programação principal
- **Flask**: Framework web para criar a aplicação
- **Pandas**: Biblioteca para manipulação de dados
- **Jinja2**: Motor de templates utilizado pelo Flask
- **HTML/CSS**: Para a interface do usuário

### Estrutura do projeto

A estrutura do projeto é a seguinte:

meu_projeto/ │ ├── app.py # Script principal da aplicação ├── banco/ # Pasta contendo arquivos de dados │ └── BaseFuncionarios.xlsx # Arquivo Excel com dados └── templates/ # Pasta contendo templates HTML └── index.html # Página principal


---

## Como criar um executável

Para criar um executável da sua aplicação, siga os passos abaixo:

### Passo 1: Instale o PyInstaller

    *** Se você ainda não tem o PyInstaller instalado, execute o seguinte comando:***   
    ```bash
    pip install pyinstaller

    pyinstaller --onefile --add-data "templates:templates" agent.py



### Dicas para Personalizar

- Substitua os espaços reservados (como "[descrever brevemente...]" e "[Outros recursos, se houver]") com informações específicas sobre o seu projeto.
- Adicione imagens, badges ou links relevantes que possam enriquecer a documentação.
- Considere incluir uma seção sobre como configurar um ambiente virtual, instalar dependências e rodar a aplicação em modo de desenvolvimento, se aplicável.

Sinta-se à vontade para ajustar o conteúdo para que ele reflita melhor seu projeto e estilo!

