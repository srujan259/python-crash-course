srujan = {'good':'hardworking', 'bad': 'procastinates'}
del srujan['bad']
print(srujan)
Value = srujan.get('bad', 'No bad qualities')
print(Value)