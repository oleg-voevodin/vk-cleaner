import vk_api
import time

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

    while vk.wall.get()['count'] != 0:
        for post in vk.wall.get(count=100)['items']:
            vk.wall.delete(post_id=post['id'])
            time.sleep(2)

    print('Completed!')
except KeyboardInterrupt:
    print('Goodbye :D'); exit()
