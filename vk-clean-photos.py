import vk_api

login = input('Enter VK login: ')
password = input('Enter VK password: ')
try:
    try:
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
    except vk_api.exceptions.BadPassword:
        print('Bad password!'); exit()
    except vk_api.exceptions.AuthError:
        vk_session = vk_api.VkApi(login, password, auth_handler = lambda: [input('Enter two-factor auth code: '), False])
        vk_session.auth()

    vk = vk_session.get_api()

    while vk.photos.getAll()['count'] != 0:
        for photo in vk.photos.getAll(count=200)['items']:
            vk.photos.delete(photo_id=photo['id'])
   
    while vk.photos.getAlbums()['count'] != 0:
        for album in vk.photos.getAlbums()['items']:
            vk.photos.deleteAlbum(album_id=album['id'])

    print('Completed!')
except KeyboardInterrupt:
    print('Goodbye :D'); exit()
