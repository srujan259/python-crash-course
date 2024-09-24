print("----- Hey I am talking parrot! -----")

prompt = "Tell me something and ill repeat it for you: "
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    if message!= 'quit':
        print(message)
    else:
        active = False