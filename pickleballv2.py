# List of players
players = ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5', 'Player 6', 'Player 7', 'Player 8', 'Player 9', 'Player 10', 'Player 11', 'Player 12']

# Shuffle the players to generate random pairings
import random
random.shuffle(players)

# Create a list of rounds
rounds = []

# Create the rounds
for i in range(10):
  team1 = (players[i], players[(i+1) % len(players)])
  team2 = (players[(i+2) % len(players)], players[(i+3) % len(players)])
  rounds.append((team1, team2))

# Print the rounds
for i in range(10):
  round_num = i + 1
  team1 = players[i*2] + ' + ' + players[(i*2+1) % len(players)]
  team2 = players[(i*2+2) % len(players)] + ' + ' + players[(i*2+3) % len(players)]
  print('Round %d - %s vs. %s' % (round_num, team1, team2))
