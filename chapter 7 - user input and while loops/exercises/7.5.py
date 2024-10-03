prompt = "how old are you!"
prompt += "\nenter quit when done"
action = True
while action:
    age = input(prompt)
    if age == 'quit':
        action=False
    
    age = int(age)
    if(age<3):
        print('Its Free')
    elif(age>3 and age<12):
        print('Its 10$')
    else:
        print('Its 15$')
