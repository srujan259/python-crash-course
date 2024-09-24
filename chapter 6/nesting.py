aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'speed' :'fast', 'points': '5'}
    aliens.append(new_alien)


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 1

for alien in aliens[:5]:
    print(alien)

#

aliens = [{'name':'srujan','age': 20}, {'name': 'ancy', 'age': 30}]

