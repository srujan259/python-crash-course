alien = {'color':'green', 'points':5}
print(alien['color'])
print(alien['points'])

alien['x_position'] = 0
alien["y_position"] = 25
print(alien)

alien['speed'] = 'fast'
print(alien)

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
elif alien['speed'] == 'fast':
    x_increment = 3

alien['x_position'] = alien['x_position'] + x_increment
print(alien)