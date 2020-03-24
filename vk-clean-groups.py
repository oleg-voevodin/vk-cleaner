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

    print(f'Found {vk.groups.get()["count"]} groups.')

    while vk.groups.get(count=1000)['count'] != 0:
        for group_id in vk.groups.get(count=1000)['items']:
            vk.groups.leave(group_id=group_id)

    print('Completed!')
except KeyboardInterrupt:
    print('Goodbye :D'); exit()
