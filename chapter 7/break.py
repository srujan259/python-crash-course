prompt = 'Hey whats your fav city'
prompt += '\n Type quit to exit'
while True:
    fav = input(prompt)
    if fav == 'quit':
        break
    else:
        print(fav)
    
