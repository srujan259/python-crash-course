favourite_places = {'sujay': ['korea', 'hyd'], 'srujan':['hyd','nzb'], 'ancy':['kerala', 'goa']}
for name , places in favourite_places.items():
    print(f"{name} fav places are:")
    for place in places:
        print(f'\t {place}')