import random

class Wheel:

  def __init__(self, name):
    self.name = name
    self.entries = {}
    self.numbers = []
    self.wheels = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia"]

  def __repr__(self):
     description = f"The results for the cities extractions are: {self.entries}"
     return description

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
    self.bet = 0
    self.prize = 0
    self.cities = []
    self.numbers = []
  
  def __repr__(self):
     description = "Player " + self.name + " played theese cities: " + ' '.join(map(str, self.cities)) + " with the numbers: " + ' '.join(map(str, self.numbers)) + " betting $" + str(self.bet) + " with the game mode: " + self.game_mode + " and won: $" + str(self.prize)
     return description 

  def set_bet(self, bet):
    self.bet = bet
    
  def set_prize(self, prize):
    self.prize += prize
  
  def check_game_mode(self, game_mode):
    if game_mode == 'Single' or game_mode == 'Ambo' or game_mode == 'Terno' or game_mode == 'Quaterna' or game_mode == 'Cinquina':
       return True
    else:
       return False
  
  def check_numbers(self):
    for num in self.numbers:
      if num > 99 or num < 1:
        self.numbers.remove(num)
        print("Invalid number, enter a number between 1 and 99. Removing...")


print("Welcome to the Italian Lottery!")
# player objects list
players = []
counter = 1
player_number = int(input("Enter player numbers: ")) +1
while counter < player_number:
    player_name = input("Enter player" + str(counter) + " name: ")
    # player is instantiated
    player = Player(player_name)
    players.append(player)
    count = 0
    print("Enter up to 10 cities...enter '0' when done.")
    while True and count < 10:
        user_city = input("Enter player"+ str(counter) + " cities: ")
        if user_city == "0":
            count1 = 0
            while True:
                game_mode = input("Enter a play mode between: 'Single', 'Ambo', 'Terno', 'Quaterna', 'Cinquina': ")
                if player.check_game_mode(game_mode):
                   player.game_mode = game_mode
                   break
                else:
                   print("Invalid game mode!")
            print("Enter up to 10 numbers between 1 and 99...enter '0' when done.")
            while True and count1 < 10:
                user_number = int(input("Enter player" + str(counter) + " numbers: "))
                if user_number == 0:
                    while True:
                        user_bet = int(input("Enter player" + str(counter) + " bet from $1 up to $200: "))
                        player.bet = user_bet
                        break
                    break
                else:
                    player.check_numbers()
                    player.numbers.append(user_number)
                    count1 += 1
            break
        else:
            player.cities.append(user_city)
    counter += 1
    
def check_guessed_numbers():
  for player in players:
      for city in wheel.entries:
          # if I find a player city match
          if player.cities.count(city) >= 1:
              for number in player.numbers:
                  # if I find a number match for city match
                  if wheel.entries[city].count(number) >= 1 and player.game_mode == 'Single':
                      if len(player.numbers) == 10:
                         prize = (1.12 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 9:
                         prize = (1.25 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 8:
                         prize = (1.40 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 7:
                         prize = (1.60 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 6:
                         prize = (1.87 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 5:
                         prize = (2.25 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 4:
                         prize = (2.81 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 3:
                         prize = (3.74 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 2:
                         prize = (5.62 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 1:
                         prize = (11.23 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                         print(player.name, wheel.entries[city])
                         print(player.name + " won " + "$ "+ str(round(player.prize, 2)))
                         break
                  elif wheel.entries[city].count(number) >= 2 and player.game_mode == 'Ambo':
                      if len(player.numbers) == 10:
                         prize = (5.56 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 9:
                         prize = (6.94 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 8:
                         prize = (8.93 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 7:
                         prize = (11.90 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 6:
                         prize = (16.67 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 5:
                         prize = (25 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 4:
                         prize = (41.67 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 3:
                         prize = (83.33 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 2:
                         prize = (250 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                         break
                  elif wheel.entries[city].count(number) >= 3 and player.game_mode == 'Terno':
                      if len(player.numbers) == 10:
                         prize = (37.50 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 9:
                         prize = (53.57 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 8:
                         prize = (80.36 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 7:
                         prize = (128.57 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 6:
                         prize = (225 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 5:
                         prize = (450 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 4:
                         prize = (1125 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 3:
                         prize = (4500 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                         break
                  elif wheel.entries[city].count(number) >= 4 and player.game_mode == 'Quaterna':
                      if len(player.numbers) == 10:
                         prize = (571.43 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 9:
                         prize = (952.38 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 8:
                         prize = (1714.29 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 7:
                         prize = (3428.57 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 6:
                         prize = (8000 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 5:
                         prize = (24000 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 4:
                         prize = (120000 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                         break
                  elif wheel.entries[city].count(number) >= 5 and player.game_mode == 'Cinquina':
                      if len(player.numbers) == 10:
                         prize = (23809.52 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 9:
                         prize = (47619.05 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 8:
                         prize = (107142.86 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 7:
                         prize = (285714.29 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 6:
                         prize = (1000000 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                      elif len(player.numbers) == 5:
                         prize = (6000000 * player.bet) / (len(player.cities))
                         player.set_prize(prize)
                         print("You just won "+"$ "+ str(round(prize, 2)))
                         break
      print(repr(player))
                
              
# numbers are exctracted from cities
wheel.get_numbers()
wheel.populate_numbers()
wheel.populate_entries()
print(repr(wheel))
# check player guesses
check_guessed_numbers()

    


