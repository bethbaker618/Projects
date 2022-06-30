# You are a physics teacher preparing for the upcoming semester. 
# You want to provide your students with some functions that will help them calculate some fundamental physical properties.


def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return c_temp

f100_in_celsius = 100
print(f_to_c(f100_in_celsius))

c0_in_fahrenheit = 0
print(f_to_c(c0_in_fahrenheit))

def get_force(mass, acceleration):
  return mass*acceleration

train_mass = 1000
train_acceleration = 12
train_distance = 30
print('The GE train supplies ' + str(get_force(train_mass, train_acceleration)) + ' Newtons of force.')

def get_energy(mass, c = 3*10**8):
  return mass*c**2

bomb_mass = 50
bomb_energy = get_energy(bomb_mass)
print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules.')

def get_work(mass, acceleration, distance):
  force = get_force(train_mass, train_acceleration)
  work = force*distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)
print('The GE train does ' + str(train_work) + ' Joules of work over ' + str(train_distance) + ' meters.')