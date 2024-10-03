sandwich_orders = ['club', 'spicy', 'cheesy', 'pastrami', 'pastrami', 'pastrami']
finished_orders = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f'I made you a {current_order} sandwich')
    finished_orders.append(current_order)

print('below sandiwches were made')
for s in finished_orders:
    print(s)