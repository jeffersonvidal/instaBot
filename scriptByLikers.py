from instapy import InstaPy #importando biblioteca InstaPy
from instapy import smart_run #importando dependência da InstaPy

#iniciando sessão
session = InstaPy(username='', password='') #usuário e senha do perfil do instagram

#configuração
with smart_run(session):
    #habilitando o programa para seguir pessoas e 
    #informando qual a porcentagem ele deve seguir. 
    #Ex: 100 = 100% dos usuários que ele encontrar
    session.set_do_follow(enabled = True, percentage = 100)
    #habilitar o programa a dar like nos perfis e seguir a porcentagem informada
    session.set_do_like(enabled = True, percentage = 100)
    #habilitar o programa dar like por tags (tags como referência)
    #verificar se existe a hashtag que deseja seguir e depois informar no programa
    #session.like_by_tags([hashtag a se seguida], qtd de fotos que é pra curtir)
    #recomendado não colocar mais que 800 fotos para serem curtidas na mesma execução
    #amount = qtd a interagir, unfollow = deixar de seguir o perfil, interact = considerar comentarios e likes no post
    #->session.like_by_tags(['udemy'], amount=5) #interage pela hashtag
    #->session.like_by_feed(amount = 3, randomize = True, unfollow = False, interact = True) #interage pelo feed
    #deve pesquisar no instagram pela localização (com icone do google maps) a cidade desejada
    #https://www.instagram.com/explore/locations/881089121/montes-claros-minas/
    #deve copiar o código após https://www.instagram.com/explore/locations/
    #pode usar várias cidades ao mesmo tempo
    #->session.like_by_locations(['249617615/sao-paulo/'], amount = 3) #interage por localização (cidade)

    #Mostrar para seguidores de seus seguidores que você tem algo interessante ou similar
    #inserir o nome de perfil do seu seguidor, pode usar vários simultaneamente separar por vírgula ['fulano','ciclano']
    #->session.follow_user_followers(['isetups'], amount = 3, randomize = False) #segue seguidores de outros perfis
    #->session.follow_user_following(['isetups'], amount = 3, randomize = False) #seguir usuários que esse perfil segue também

    #Segue quem comentou ou curtiu um post ou perfil específico
    #pode usar vários simultaneamente ['fulano','ciclano']
    #photos_grab_amount = qtd de fotos p/ verificar quantos seguidores ele tem
    #follow_likers_per_photo = qtd de pessoas eu quero seguir
    #sleep_delay = tempo (em segundos) de espera o robô ficará aguardando para próximas execuções para enganar o instagram
    session.follow_likers(['isetups'], photos_grab_amount = 2, follow_likers_per_photo = 2, randomize = True, sleep_delay = 600, interact = True)


    #qual será o comentario deixado nas fotos
    comentarios = ['Muito bom!', 'Belo post']
    #habilitar para comentar nos posts encontrados
    #informar porcentagem de posts que ele vai comentar
    session.set_do_comment(enabled = True, percentage = 90)
    #postar efetivamente os comentários, onde ele deve comentar (fotos, videos)
    session.set_comments(comentarios, media = 'Photo')
    #interagir com algorítmo do instagram
    session.join_pods()
