numbers = list(range(1,10))
for n in numbers:
    if n == 1:
        print(f'{n}st')
    elif n ==2:
        print(f'{n}nd')
    elif n == 3:
        print(f'{n}rd')
    else:
        print(f'{n}th')