sandwich_orders = ['club', 'spicy', 'cheesy', 'pastrami', 'pastrami', 'pastrami']
print('OOp we ran out of pastrami!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_san = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'working on you {current_sandwich} sandwich')
    finished_san.append(current_sandwich)

for sand in finished_san:
    print(sand)