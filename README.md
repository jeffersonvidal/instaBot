<h1 align="center">
    <img alt="InstaBot" src="./screenshots/logo.jpg"  width="400px"/>
</h1>

<h3 align="center" >
  InstaBot
</h3>

<p align="center">
    Robô criado para engajar e interagir com seguidores e perfis no Instagram.

    Por meio de curtidas e comentários em fotos e seguindo perfis alvos, vamos dizer para o robô divulgar meu perfil para uma quantidade enorme de usuários e atingir maior engajamento.
</p>

<p align="center">
  <img alt="Languagues" src="https://img.shields.io/github/languages/count/jeffersonvidal/instaBot">
  <img alt="Top Languague" src="https://img.shields.io/github/languages/top/jeffersonvidal/instaBot">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jeffersonvidal/instaBot">
  <a href="https://github.com/jeffersonvidal/foodfy/commits/master">
    <img alt="Last commit date" src="https://img.shields.io/github/last-commit/jeffersonvidal/instaBot">
  </a>
  <a href="https://github.com/jeffersonvidal/instaBot" target="_blank">
    <img alt="GitHub license" src="https://img.shields.io/github/license/jeffersonvidal/instaBot">
  </a>
</p>
<p align="center">
  <a href="https://github.com/jeffersonvidal/instaBot/issues" target="_blank">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/jeffersonvidal/instaBot"></a>
  <a href="https://github.com/jeffersonvidal/instaBot/network" target="_blank">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/jeffersonvidal/instaBot">
  </a>
  <a href="https://github.com/jeffersonvidal/instaBot/stargazers" target="_blank">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/jeffersonvidal/instaBot">
  </a>
  <a href="https://github.com/jeffersonvidal" target="_blank">
    <img alt="Made by Jefferson Vidal" src="https://img.shields.io/badge/made%20by-jeffersonvidal-informational">
  </a>
  <a href="https://www.linkedin.com/in/jeffersonvidal/" target="_blank" >
    <img alt="Linkedin - Jefferson Vidal" src="https://img.shields.io/badge/Linkedin--%23F8952D?style=social&logo=linkedin">
  </a>
  <a href="https://api.whatsapp.com/send?phone=5538988294043"
        target="_blank" >
    <img alt="Fale comigo no whatsapp - Jefferson Vidal" src="https://img.shields.io/badge/Whatsapp--%23F8952D?style=social&logo=whatsapp">
  </a>
</p>

<p align="center">
  <a href="#utilizacao">Utilização</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#funcionalidades">Funcionalidades</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#license">Licença</a>
</p>

<a id="utilizacao"></a>
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

<a id="funcionalidades"></a>
### Funcionalidades
- [x] Localização - segue e comenta de acordo a região (cidade) informada;
- [x] Curtidas e comentários - segue quem comentou e/ou curtiu fotos de um perfil;
- [x] Feed - segue e comenta nas postagens do feed principal do instagram;
- [x] Hashtags - segue e comenta com hashtags definidas por você;
- [x] Perfis de seguidores - segue seguidores de outros perfis;
- [x] Parar de seguir perfis;

<a id="tecnologias"></a>
### Tecnologias e bibliotecas utilizadas

- [x] InstaPy - https://github.com/timgrossmann/InstaPy
- [x] Documentação - https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md

<a id="instalacao"></a>
### Instalação

- [x] Python 3.8.2 - https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe

Executar os comandos abaixo no prompt de comando ou terminal.

~~~
python -m pip install --upgrade pip
pip install --upgrade setuptools
pip install instapy
pip install protobuf==3.6.0 - (Caso dê o problema de DLL)
~~~

<a id="license"></a>
## License

This project is under MIT. See at here [LICENSE](/LICENSE) for more informations.

---

Made by :blue_heart: [Jefferson Vidal](https://github.com/jeffersonvidal)