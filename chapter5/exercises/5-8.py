usernames = ['admin', 'bob', 'snoopy', 'jimmy', 'muthu']
# usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin would you like to see the status report')
        else:
            print(f'Hello {user} thank you for logging in again')
else:
    print('We need to find some users')
    
