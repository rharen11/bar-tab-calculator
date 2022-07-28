ninjas = ['bob', 'steve', 'joe']

# for ninja in ninjas:
#   print(ninja)

# for ninja in ninjas[1:3]:
#   print(ninja)

for ninja in ninjas:
  if ninja == 'bob':
    print(f'{ninja} - black belt')
    break
  else:
    print(ninja)