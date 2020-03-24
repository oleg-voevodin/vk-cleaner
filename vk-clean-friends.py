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

    print(f'Found {vk.friends.get()["count"]} friends.')

    while vk.friends.get()['count'] != 0:
        for user_id in vk.friends.get(count=10000)['items']:
            vk.friends.delete(user_id=user_id)
   
    while vk.friends.getRequests(out=1)['count'] != 0:
        for user_id in vk.friends.getRequests(count=1000, out=1):
            vk_friends.delete(user_id=user_id)

    vk.friends.deleteAllRequests()

    print('Completed!')
except KeyboardInterrupt:
    print('Goodbye :D'); exit()
