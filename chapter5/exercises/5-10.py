current_users = ['admin', 'bob', 'snoopy', 'jimmy', 'muthu']
new_users = ['srujan', 'boB', 'sujaY', 'sowmya']

current_users_lowercase = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lowercase:
        print(f'{user} needs to use another username')
    else:
        print(f'{user} is available')
