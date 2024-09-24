name_prompt = "whats your name"
place_prompt = "If you could visit one place in the world, where would you go?"
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

active = True
responses = {}
while active:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

for name , place in responses.items():
    print(f"{name} wants to visit {place}")
