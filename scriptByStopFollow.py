from instapy import InstaPy #importando biblioteca InstaPy
from instapy import smart_run #importando dependência da InstaPy

#iniciando sessão
session = InstaPy(username='', password='') #usuário e senha do perfil do instagram

#configuração
with smart_run(session):
    #Parar de seguir os perfis
    #style = critério para parar de seguir, opções abaixo:
    #with "FIFO", it will unfollow users in the exact order they are loaded ("FIFO" is the default style unless you change it);
    #with "LIFO" it will unfollow users in the reverse order they were loaded;
    #with "RANDOM" it will unfollow users in the shuffled order;
    #unfollow_after = tempo que você segue o perfil, tempo em segundos. Ex: 3hrs = 3*60*60
    #->session.unfollow_users(amount = 2, allFollowing = True, style = FIFO, unfollow_after = 3*60*60, sleep_delay = 450)
    
    #Parar de seguir quem não segue seu perfil
    session.unfollow_users(amount = 2, nonFollowers = True, style = FIFO, unfollow_after = 3*60*60, sleep_delay = 450)

    #qual será o comentario deixado nas fotos
    comentarios = ['Muito bom!', 'Belo post','Muito bom!', 'Belo post','Muito bom!', 'Belo post','Muito bom!', 'Belo post','Muito bom!', 'Belo post']
    #habilitar para comentar nos posts encontrados
    #informar porcentagem de posts que ele vai comentar
    session.set_do_comment(enabled = True, percentage = 90)
    #postar efetivamente os comentários, onde ele deve comentar (fotos, videos)
    session.set_comments(comentarios, media = 'Photo')
    #interagir com algorítmo do instagram
    session.join_pods()
