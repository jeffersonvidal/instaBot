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
    session.like_by_tags(['udemy'], amount=5) #interage pela hashtag
    #qual será o comentario deixado nas fotos
    comentarios = ['Muito bom!', 'Belo post']
    #habilitar para comentar nos posts encontrados
    #informar porcentagem de posts que ele vai comentar
    session.set_do_comment(enabled = True, percentage = 90)
    #postar efetivamente os comentários, onde ele deve comentar (fotos, videos)
    session.set_comments(comentarios, media = 'Photo')
    #interagir com algorítmo do instagram
    session.join_pods()
