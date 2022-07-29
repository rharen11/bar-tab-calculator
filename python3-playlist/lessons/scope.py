my_name = 'rachel'

def print_name():
  global my_name
  my_name = 'steve'
  print('the name inside the function is'.my_name)

print_name()
print('outside the function the name is'.my_name)