import vk_api
import time

def delete_in_subs():
    if vk.users.getFollowers()['count'] == 0:
        print('You haven\'t incoming subscriptions.')
        return None
    print('All subscribers will be blocked for 20 minutes, then they will be remove from blacklist. No, I\'m not dummy, VK have some things, what fuck my brain :D')
    choice = input('ENTER \'YES\' FOR CONTINUE: ')
    if choice.lower() != 'yes':
        print('Exiting..'); exit()
    subscribers = []
    while vk.users.getFollowers()['count'] != 0:
        for user_id in vk.users.getFollowers(count=1000)['items']:
            subscribers.append(user_id)
        print('Blocking..')
        for user_id in subscribers:
            vk.account.ban(user_id=user_id)
            time.sleep(2)
    print('All subscribers blocked. After 20 mins they will be removed from blacklist.')
    time.sleep(1200)
    for user_id in subscribers:
        vk.account.unban(user_id=user_id)
    print('All subscribers unbanned.')

def delete_out_subs():
    while vk.users.getSubscriptions()['users']['count'] != 0:
        print('Deleting users subscriptions...')
        for user_id in vk.users.getSubscriptions(count=200)['users']['items']:
            vk.friends.delete(user_id=user_id)
            time.sleep(2)
    while vk.users.getSubscriptions()['groups']['count'] != 0:
        print('Deletins groups subscriptions...')
        for group_id in vk.users.getSubscriptions(count=200)['groups']['items']:
            vk.groups.leave(group_id=group_id)
            time.sleep(2)
    print('All subscriptions deleted.')

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
    
    choice = input('Enter 0 for delete all subscriptions\nEnter 1 for delete incoming subscriptions only\nEnter 2 for delete outgoing subscriptions only\n\nYou choice:')
    
    if choice == '0':
        delete_in_subs()
        delete_out_subs()
    elif choice == '1':
        delete_in_subs()
    elif choice == '2':
        delete_out_subs()
    else:
        print('Unknown choice. Goodbye :D')

    print('Completed!')
except KeyboardInterrupt:
    print('Goodbye :D'); exit()
