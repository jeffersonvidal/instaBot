# InstaBot

Robô criado para engajar e interagir com seguidores e perfis no Instagram.

Por meio de curtidas e comentários em fotos e seguindo perfis alvos, vamos dizer para o robô divulgar meu perfil para uma quantidade enorme de usuários e atingir maior engajamento.

## Utilização

* Informar os dados de usuário e senha do seu perfil do instagram no arquivo de script;
* Executar de forma manual: 
    - Abrir o prompt de comando ou terminal na pasta do projeto e digitar o comando: python nomeDoScript.py e pressionar enter;
* Executar de forma automática: 
    - Criar um arquivo "instaBot.bat" contendo o comando python: python nomeDoScript.py
    - No MS Windows, abrir o aplicativo "Agendados de Tarefas";
    - No menu esquerdo click em Microsoft;
    - No canto direito click em Criar tarefa;
    - Na aba Geral, dar um nome para tarefa "Robô Instagram", em descrição pode colocar do que se trata a tarefa, marque a opção "Executar estando o usuário conectado ou não", depois marque a opção "Executar com privilégios mais altos", marque a opção "Oculto";
    - Na aba Disparadores, click em Novo, defina como "Diário", ajuste a hora de execução e sincronizar o fuso horário;
    - Na aba Ações, click em Novo, "Iniciar um programa", procurar pelo "instaBot.bat", em "Iniciar em" informa a pasta dos arquivos dos scripts.py, onde está o projeto junto com o instaBot.bat;
    - Salve e confirme tudo e pronto;

### Funcionalidades
- [x] Localização - segue e comenta de acordo a região (cidade) informada;
- [x] Curtidas e comentários - segue quem comentou e/ou curtiu fotos de um perfil;
- [x] Feed - segue e comenta nas postagens do feed principal do instagram;
- [x] Hashtags - segue e comenta com hashtags definidas por você;
- [x] Perfis de seguidores - segue seguidores de outros perfis;
- [x] Parar de seguir perfis;

### Tecnologias e bibliotecas utilizadas

- [x] InstaPy - https://github.com/timgrossmann/InstaPy
- [x] Documentação - https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md

### Instalação

- [x] Python 3.8.2 - https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe

Executar os comandos abaixo no prompt de comando ou terminal.

~~~
python -m pip install --upgrade pip
pip install --upgrade setuptools
pip install instapy
pip install protobuf==3.6.0 - (Caso dê o problema de DLL)
~~~