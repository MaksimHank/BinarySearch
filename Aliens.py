alien = {
    'loc x': 15,
    'loc y': 40,
    'color': 'green',
    'health': 100,
    'name': 'pupsik',
    'points': 10
}

aliens = []

for each_alien in range (0, 20):
    aliens.append(alien.copy())

for i in aliens:
    print(i)


print('\n----------------------------------------')
aliens[7]['loc x'] += 50
aliens[12]['health'] = 2

for i in aliens:
    print(i)