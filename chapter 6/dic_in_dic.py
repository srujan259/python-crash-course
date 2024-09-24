username = {
    'ksrujan': {
        'first_name': 'srujan',
        'last_name': 'kumar',
        'location': 'hyd'
    },
    'ajohn': {
        'first_name': 'ancy',
        'last_name': 'john',
        'location': 'kerala'
    }
}

for user, details in username.items():
    print(f'Details of {user.title()}')
    print(f"\tfull name : {details['first_name']} {details['last_name']}")
    print(f"\tlocation: {details['location']}")
        