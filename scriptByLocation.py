from instapy import InstaPy #importando biblioteca InstaPy
from instapy import smart_run #importando dependência da InstaPy

#iniciando sessão
session = InstaPy(username='', password='') #usuário e senha do perfil do instagram

#configuração
with smart_run(session):
    #deve pesquisar no instagram pela localização (com icone do google maps) a cidade desejada
    #https://www.instagram.com/explore/locations/881089121/montes-claros-minas/
    #deve copiar o código após https://www.instagram.com/explore/locations/
    #pode usar várias cidades ao mesmo tempo
    session.like_by_locations(['249617615/sao-paulo/'], amount = 3) #interage por localização (cidade)
    #qual será o comentario deixado nas fotos
    comentarios = ['Muito bom!', 'Belo post']
    #habilitar para comentar nos posts encontrados
    #informar porcentagem de posts que ele vai comentar
    session.set_do_comment(enabled = True, percentage = 90)
    #postar efetivamente os comentários, onde ele deve comentar (fotos, videos)
    session.set_comments(comentarios, media = 'Photo')
    #interagir com algorítmo do instagram
    session.join_pods()
