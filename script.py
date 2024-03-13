import random

class Wheel:

  def __init__(self, name):
    self.name = name
    self.entries = {}
    self.numbers = []
    self.wheels = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]

  def get_numbers(self):
    numbs = []
    while len(numbs) < 5:
      rand_num = random.randint(1, 99)
      numbs.append(rand_num)
    return numbs
  
  def populate_numbers(self):
    for num in range(len(self.wheels)):
      self.numbers.append(self.get_numbers())

  def populate_entries(self):
    self.entries.update({key:value for key, value in zip(self.wheels, self.numbers)})

# first instance of Wheel
wheel = Wheel("First Wheel")

class Player:

  def __init__(self, name):
    self.name = name
    self.wheels = []
    self.numbers = []

def check_guessed_numbers():
  player_entries = []
  for key in wheel.entries:
    for wheels in player.wheels:
      if key == wheels:
        player_entries.append(wheel.entries[key])
  print(player_entries)
  for numbers in player_entries:
    num_to_string = str(numbers)
    print(numbers)
    if player.numbers in num_to_string:
      print("you have an entry")


def get_player_numbers():
  print("Choose up to 10 numbers between 1 and 99\n digit 'done' to confirm: ")
  while len(player.numbers) < 10:
    player_numbers = input()
    if player_numbers == "done":
      print(player.numbers)
      print(player.wheels)
      # when the player is done with the numbers
      # extraction of numbers start
      wheel.get_numbers()
      wheel.populate_numbers()
      wheel.populate_entries()
      # check if player guessed a number
      check_guessed_numbers()
    else:
       player.numbers.append(player_numbers)






player_input = input("Welcome to the Italian Lottery!\nEnter your name: ")
# player is instantiated
player = Player(player_input)
print("Welcome " + player.name + "...")
# get the player wheels to play with
string_wheels = ''
for names in wheel.wheels:
  string_wheels += names + ' '

print("Choose up to 10 wheels from: " + string_wheels + "digit 'done' to confirm")
while len(player.wheels) < 10:
  wheels_input = input()
  if wheels_input == "done":
    get_player_numbers()
    
  elif wheels_input == "Bari":
    player.wheels.append(wheels_input)
    print(player.wheels)
  elif wheels_input == "Cagliari":
    player.wheels.append(wheels_input)
  elif wheels_input == "Firenze":
     player.wheels.append(wheels_input)
  elif wheels_input == "Genova":
     player.wheels.append(wheels_input)
  elif wheels_input == "Milano":
     player.wheels.append(wheels_input)
  elif wheels_input == "Napoli":
     player.wheels.append(wheels_input)
  elif wheels_input == "Palermo":
     player.wheels.append(wheels_input)
  elif wheels_input == "Roma":
     player.wheels.append(wheels_input)
  elif wheels_input == "Torino":
     player.wheels.append(wheels_input)
  elif wheels_input == "Venezia":
     player.wheels.append(wheels_input)
  else:
    print("Enter a valid wheel")


