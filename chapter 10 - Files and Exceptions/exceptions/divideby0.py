try:
    5/0
except (ZeroDivisionError) as e :
    print(f'Bro you cant divide by 0 - {e}')