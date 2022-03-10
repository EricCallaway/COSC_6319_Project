message = "Hello World"
print(message)
message = "Pyhton crash course"
print(message)

first_name = "Navya"
last_name = "makkena"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name}")

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

print(5+3)
print(5+333)
print(5*3)
print(5**3)
# Say hello

import this

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(1, 'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars,reverse=True))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print(len(cars))

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician)
 print(f"my  {magician}")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

for value in range(1, 5):
  print(value)
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
 square = value ** 2
 squares.append(square)
print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**3 for value in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])#last three players on the roster

for player in players[:3]:
 print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # copying the list
print(friend_foods)

#Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
 print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
 if(car == 'bmw'):
     print(car.upper())
 else:
     print(car.title())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print( 'mushrooms' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 12
if age < 4:
       print("Your admission cost is $0.")
elif age < 18:
       print("Your admission cost is $25.")
else:
       print("Your admission cost is $40.")

age = 12

if age < 4:
       price = 0
elif age < 18:
       price = 25
elif age < 65:
       price = 40
elif age >= 65:
       price = 20

print(f"Your admission cost is ${price}.")


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
           print(f"Adding {requested_topping}.")
           print("\nFinished making your pizza!")
else:
       print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                         'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
   if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
   else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")


# dictionary is a group of key value pairs
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
del alien_0['points']
print(alien_0)
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
point_value = alien_0.get('y_position')
print(point_value)

user_0 = {
       'username': 'efermi',
       'first': 'enrico',
       'last': 'fermi',
       }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for name in user_0.keys():
       print(name.title())
for name in user_0.values():
       print(name.title())
for name in sorted(user_0.keys()):
       print(name.title())


languages = {'python', 'ruby', 'python', 'c'}
print(languages)

aliens = []

   # Make 30 green aliens.
for alien_number in range(30):
     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
     aliens.append(new_alien)

   # Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
    print("...")

   # Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

"""message = input("Tell me something, and I will repeat it back to you: ")
print(message)


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")"""

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#functions

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello! {username}")

greet_user("Navya")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')


def get_formatted_name(first_name, last_name):
       """Return a full name, neatly formatted."""
       full_name = f"{first_name} {last_name}"
       return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
       """Return a full name, neatly formatted."""
       if middle_name:
           full_name = f"{first_name} {middle_name} {last_name}"
       else:
           full_name = f"{first_name} {last_name}"
       return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name):
       """Return a dictionary of information about a person."""
       person = {'first': first_name, 'last': last_name}
       return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

def make_pizza(*toppings):
     print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
     user_info['first_name'] = first
     user_info['last_name'] = last
     return user_info

user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)

""" import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents) """