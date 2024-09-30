def build_profile(first, last, **user_details):
    """ function to build profile """
    user_details['first_name'] = first
    user_details['last_name'] = last
    return user_details


user = build_profile('srujan', "kottapally", location='hyderabad', field='IT')
print(user)