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
      if numbs.count(rand_num) >= 1:
        numbs.remove(rand_num)
      else:
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
    self.game_mode = ''
    self.bet = 1
    self.prize = 0
    self.wheels = []
    self.numbers = []

  def set_bet(self, bet):
    self.bet = bet
    
  def set_prize(self, prize):
    self.prize += prize
  
  def set_game_mode(self, mode):
    self.game_mode = mode
  
  def check_numbers(self):
    for num in self.numbers:
      if num > 99 or num < 1:
        self.numbers.remove(num)
        print("Invalid number, removed...")


def check_guessed_numbers():
  for keys in wheel.entries:
    for city in player.wheels:
      if keys == city:
        for number in player.numbers:
          if wheel.entries[city].count(number) >= 1 and player.game_mode == "single":
            if len(player.numbers) == 10:
              prize = (1.12 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 9:
              prize = (1.25 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 8:
              prize = (1.40 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 7:
              prize = (1.60 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 6:
              prize = (1.87 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 5:
              prize = (2.25 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 4:
              prize = (2.81 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 3:
              prize = (3.74 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 2:
              prize = (5.62 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            elif len(player.numbers) == 1:
              prize = (11.23 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+ str(round(prize, 2)))
            print(keys, wheel.entries[city])
            print("You won " + "$ "+ str(round(player.prize, 2)))
            break
          elif wheel.entries[city].count(number) >= 2 and player.game_mode == "ambo":
            if len(player.numbers) == 10:
              prize = (5.56 * player.bet) / (len(player.wheels) +1)
              player.set_prize(prize)
              print("You just won "+"$ "+prize)

player_input = input("Welcome to the Italian Lottery!\nEnter your name: ")
# player is instantiated
player = Player(player_input)
print("Welcome " + player.name + "...")
# player choose the bet size
while True:
  try:
    bet = int(input("Choose you bet from $1 up to $200: "))
    if bet > 200 or bet < 1:
      print("You must enter a valid bet")
    else:
      player.set_bet(bet)
      break
  except:
    print("You must enter a valid whole number")

while True:
  game_mode = input("Choose a 'Game Mode' from 'single', 'ambo', 'terno', 'quaterna', 'cinquina': ")
  if game_mode == 'single' or game_mode == 'ambo' or game_mode == 'terno' or game_mode == 'quaterna' or game_mode == 'cinquina':
     player.set_game_mode(game_mode)
     break
  else:
    print("You must enter a valid Game Mode")

cities = ' '.join(wheel.wheels)
print("Choose up to 10 cities from: " + cities + ". Digit 'done' to confirm")
while True:
  try:
    wheels_input = input("Enter cities separated by a comma: ")
    player.wheels = [s.strip() for s in wheels_input.split(",")]
    print(player.wheels)
    break
  except:
    print("Don't forget the comma!")

print("Choose up to 10 numbers between 1 and 99: ")
while True:
  try:
    player_numbers_input = input("Enter the numbers separated by commas: ")
    print("Enter a valid number between 1 & 99")
    player.numbers = [n.strip() for n in player_numbers_input.split(",")]
    integer_conversion = [int(n) for n in player.numbers]
    player.numbers = integer_conversion
    player.check_numbers()
    break
  except:
    print("Don't forget the comma!")


# numbers are exctracted from cities
wheel.get_numbers()
wheel.populate_numbers()
wheel.populate_entries()
# check player guesses
check_guessed_numbers()

print(player.numbers)
print(player.wheels)
print(wheel.entries)
    


