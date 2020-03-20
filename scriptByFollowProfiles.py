from instapy import InstaPy #importando biblioteca InstaPy
from instapy import smart_run #importando dependência da InstaPy

#iniciando sessão
session = InstaPy(username='', password='') #usuário e senha do perfil do instagram

#configuração
with smart_run(session):
    #Mostrar para seguidores de seus seguidores que você tem algo interessante ou similar
    #inserir o nome de perfil do seu seguidor, pode usar vários simultaneamente separar por vírgula ['fulano','ciclano']
    session.follow_user_followers(['isetups'], amount = 3, randomize = False) #segue seguidores de outros perfis
    session.follow_user_following(['isetups'], amount = 3, randomize = False) #seguir usuários que esse perfil segue também


    #qual será o comentario deixado nas fotos
    comentarios = ['Muito bom!', 'Belo post']
    #habilitar para comentar nos posts encontrados
    #informar porcentagem de posts que ele vai comentar
    session.set_do_comment(enabled = True, percentage = 90)
    #postar efetivamente os comentários, onde ele deve comentar (fotos, videos)
    session.set_comments(comentarios, media = 'Photo')
    #interagir com algorítmo do instagram
    session.join_pods()
