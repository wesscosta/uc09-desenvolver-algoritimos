# **PYTHON**

> *Python é uma linguagem de programação que permite trabalhar rapidamente e integrar sistemas de forma mais eficaz.*
> 
- Introdução ao Python;
    - Livros
        
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/ad132701-ec25-4b3e-9259-9d8899736d4b/a608b6ce-9fc3-449f-a115-e4c5a0e82d6f/image.png)
        
        [Pense em Python](https://penseallen.github.io/PensePython2e/)
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/ad132701-ec25-4b3e-9259-9d8899736d4b/525c5362-9e70-4fae-910e-de58e7894072/image.png)
        
        [Python Fluente, Segunda Edição (2023)](https://pythonfluente.com/)
        
        - Artigos
            
            https://wiki.python.org.br/ListaDeExercicios
            
            https://towardsdatascience.com/python-template-string-formatting-method-df282510a87a
            
            https://pythonacademy.com.br/blog/operadores-aritmeticos-e-logicos-em-python
            
            https://www.python.org/downloads/
            
            https://www2.ufjf.br/deptocomputacao//files/2010/08/apresentacao.pdf
            
            https://medium.com/reflexão-computacional/operações-dfc579b4bd20
            
    - Introdução
        
        
        https://www.python.org/about/
        
        - **Zen of Python**
            
            ```python
            import this
            ```
            
        - O que é Python?
            - **Linguagem de Programação de Alto Nível**: Interpretada, de propósito geral, criada por Guido van Rossum e lançada em 1991.
            - **Sintaxe Simples e Clara**: Desenvolvida para ser fácil de ler e escrever, acessível tanto para iniciantes quanto para programadores experientes.
            - **Princípio do "Menor Surpreendimento"**: Projetada para minimizar a complexidade e evitar elementos confusos.
            - **Linguagem Versátil**: Suporta múltiplos paradigmas de programação (orientada a objetos, funcional e procedural).
        - Características Destacadas
            - **Biblioteca Padrão Ampla**: Conhecida como "batteries included" (baterias incluídas), oferece módulos prontos para uma ampla gama de tarefas.
            - **Flexibilidade**: Utilizada em diversas áreas como desenvolvimento web, ciência de dados, automação, scripts, inteligência artificial, e mais.
        - Razões para a Popularidade de Python
            1. **Facilidade de Aprendizado**:
            2. **Comunidade Ativa**:
            3. **Versatilidade**:
            4. **Suporte Corporativo**:
            5. **Futuro Promissor**:
        - Ferramentas on-line:
            - Jupyter Notebook
            - Google Colab
            - Replit
    - Ambiente de Desenvolvimento
        - 1. Download Python
            
            [Welcome to Python.org](https://www.python.org/)
            
        
        <aside>
        
        - **Ambientes virtuais no Python**
            
            > Criando Ambientes Virtuais em Diferentes Sistemas Operacionais
            > 
            
            Nas próximas aulas, vocês verão que eu uso o sistema operacional Windows para desenvolver e testar nossos projetos. No entanto, sei que muitos de vocês podem usar diferentes sistemas operacionais, como Linux e macOS. Por isso, preparei este guia para ajudá-los a criar e ativar ambientes virtuais em cada um desses sistemas.
            
            ### **O que é um Ambiente Virtual?**
            
            Um ambiente virtual é um espaço isolado onde você pode instalar bibliotecas e pacotes necessários para o desenvolvimento de um projeto específico, sem afetar o resto do seu sistema. Ele é especialmente útil em projetos Python, onde diferentes projetos podem precisar de diferentes versões de pacotes.
            
            ### 
            
            ### **Criando um Ambiente Virtual no Windows**
            
            1. **Abra o Prompt de Comando**:
                - Pressione `Win + R`, digite `cmd`, e pressione Enter.
            2. **Navegue até o diretório do seu projeto**:
                
                
                    `1. cd caminho\para\seu\projeto`
                
                1. 1. cd caminho\para\seu\projeto
            3. **Crie o ambiente virtual**:
                
                
                    `1. python -m venv venv`
                
                1. 1. python -m venv venv
            4. **Ative o ambiente virtual**:
                
                
                    `1. venv\Scripts\activate`
                
                1. 1. venv\Scripts\activate
            5. **Instale as dependências necessárias**:
                
                
                    `1. pip install nome_do_pacote`
                
                1. 1. pip install nome_do_pacote
            6. **Desative o ambiente virtual**:
                
                
                    `1. deactivate`
                
                1. 1. deactivate
            
            ### 
            
            ### **Criando um Ambiente Virtual no macOS**
            
            1. **Abra o Terminal**:
                - Você pode fazer isso clicando no ícone do Launchpad e digitando "Terminal".
            2. **Navegue até o diretório do seu projeto**:
                
                
                    `1. cd /caminho/para/seu/projeto`
                
                1. 1. cd /caminho/para/seu/projeto
            3. **Crie o ambiente virtual**:
                
                
                    `1. python3 -m venv venv`
                
                1. 1. python3 -m venv venv
            4. **Ative o ambiente virtual**:
                
                
                    `1. source venv/bin/activate`
                
                1. 1. source venv/bin/activate
            5. **Instale as dependências necessárias**:
                
                
                    `1. pip install nome_do_pacote`
                
                1. 1. pip install nome_do_pacote
            6. **Desative o ambiente virtual**:
                
                
                    `1. deactivate`
                
                1. 1. deactivate
            
            ### 
            
            ### **Criando um Ambiente Virtual no Linux**
            
            1. **Abra o Terminal**.
            2. **Navegue até o diretório do seu projeto**:
                
                
                    `1. cd /caminho/para/seu/projeto`
                
                1. 1. cd /caminho/para/seu/projeto
            3. **Crie o ambiente virtual**:
                
                
                    `1. python3 -m venv venv`
                
                1. 1. python3 -m venv venv
            4. **Ative o ambiente virtual**:
                
                
                    `1. source venv/bin/activate`
                
                1. 1. source venv/bin/activate
            5. **Instale as dependências necessárias**:
                
                
                    `1. pip install nome_do_pacote`
                
                1. 1. pip install nome_do_pacote
            6. **Desative o ambiente virtual**:
                
                
                    `1. deactivate`
                
                1. 1. deactivate
        </aside>
        
        - 2. **Pyenv** *(Gerenciar Versão do Python )*
            - Instalação
                - Windows
                    - Primeiramente é preciso *habilitar execução de script no powershell:*
                        - Execute o **Powershell** como **Administrador**
                        - Rode o seguinte comando no prompt: **Set-ExecutionPolicy Unrestricted**
                        - Confirme digitando “S”
                    - Instalação e Documentação
                        
                        https://github.com/pyenv-win/pyenv-win
                        
                - Linux
                    - Instalação e Documentação
                        
                        https://github.com/pyenv/pyenv
                        
            - Comandos
                - Listar as versões do Python disponível
                    
                    ```bash
                    # Para listar as versão disponivel a serem baixadas utilize o comando:
                    $ pyenv install -l 
                    
                    #para listar todas as versões do python ja baixada na maquina:
                    $ pyenv versions
                    ```
                    
                - Instalar ou Desinstalar versões do Python
                    
                    ```bash
                    # para baixa a versão do python na maquina local: utilize o seguinte comando
                    # (pode ser qualquer versão desde que disponivel):
                    $ pyenv install 3.8
                    
                    # para desinstalar alguma versão do python instalada na qua maquina:
                    $ pyenv uninstall 3.8
                    ```
                    
                - Gerenciar versão do Python no projeto
                    
                    ```bash
                    # Global
                    $ pyenv global 3.12
                    
                    #Local: Pasta do Projeto
                    $ pyenv local 3.8
                    
                    #Sistema
                    
                    ```
                    
        - 3. **env** *(Criar Ambiente Virtual)*
            - Windows
                
                ```bash
                # Crie o diretorio pelo windows explorer ou utiize o comando
                *mkdir <nomeDoProjeto>*
                
                # Criar o ambiente virtual
                python -m venv .env
                
                # Para ativar o ambiente virtual, acesse no mesmo terminal o seguinte arquivo
                .env/Scripts/activate
                ```
                
            - Linux
                
                ```bash
                # instalar o Virtualenv
                sudo apt install virtualenv
                
                # Para escolher a versão python, nome do ambiente e ativar o ambiente sao os mesmos passos do Arch linux
                ```
                
            - Arch Linux
                
                ```bash
                # instalar o Virtualenv
                sudo pacman -S python-virtualenv
                
                # Para escolher  a versão do pyhton utilizada no projeto e o nome do ambiente virtual
                virtualenv -p python3.10 .env
                
                # Para ativar o ambiente virtual, acesse no mesmo terminal o seguinte arquivo
                source .env/bin/activate
                ```
                
        - 5. **pip** *(Instalador de pacotes)*
            
            ```bash
            # Para instalar um pacote especifico
            pip install <nomeDoPacote> - <versao(opcional>
            
            # Para instalar as bibliotecas do projeto
            pip install -r requeriments.txt
            ```
            
    
    ## Sintaxe do Python
    
    [ 1. Variáveis, Tipos de Dados, Entrada e Saída, Operadores e Template Strings](https://www.notion.so/1-Vari-veis-Tipos-de-Dados-Entrada-e-Sa-da-Operadores-e-Template-Strings-2fff3eb198c380d7bed2f1f2fbcbb56b?pvs=21)
    
    [2. Estruturas Condicional, Loops, Listas, Operações Lógicas e bit a bit;](https://www.notion.so/2-Estruturas-Condicional-Loops-Listas-Opera-es-L-gicas-e-bit-a-bit-ef1bcf6323b343af97113c18fea31844?pvs=21)
    
    [3.  Listas, Dicionários, Tuplas e Funções.](https://www.notion.so/3-Listas-Dicion-rios-Tuplas-e-Fun-es-920db7f60f2a40488712cf1836bd76c1?pvs=21)
