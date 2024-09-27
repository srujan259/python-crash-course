def build_person(first_name, last_name, age=None):
    """ Return a dictionary of information about a person """
    info = {'first_name':first_name, 'last_name': last_name}
    if age:
        info['age'] = age
    return info

person = build_person('srujan', 'kottapally', 30)
print(person)