class Planet:

  shape = 'round'

  def __init__(self, name, radius, gravity, system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system

  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'

  @classmethod
  def commons(cls):
    return f'All planets are {cls.shape} because of gravity'

  @staticmethod
  def spin(speed = "2000 miles per hour"):
    return f'The planet spins and spins at {speed}'

pluto = Planet('Pluto', 30000, 8, 'Milky Way')
print(f'Name: {pluto.name}')
print(f'Radius: {pluto.radius}')
print(f'Gravity: {pluto.gravity}')
print(pluto.orbit())

print(Planet.commons())
print(pluto.spin('a very high speed'))