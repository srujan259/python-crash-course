print("----- Hey I am talking parrot! -----")

prompt = "Tell me something and ill repeat it for you: "
prompt += "\nEnter 'quit' to end the program. "

message = "" 

while message != 'quit':
    message = input(prompt)
    if message!= 'quit':
        print(message)