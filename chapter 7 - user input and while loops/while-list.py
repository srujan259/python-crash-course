unconfirmed_users = ['srujan', 'ancy', 'sujay']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'verifying user {current_user}')
    confirmed_users.append(current_user)
print('Below users have been confirmed:')
for users in confirmed_users:
    print(users)