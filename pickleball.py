import random

# Players in the pool
players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11", "Player 12"]

# List of rounds
rounds = []

# Number of rounds to play
num_rounds = 10

# Play the rounds
for i in range(num_rounds):
  # Randomly select two players for team 1
  team1_player1 = random.choice(players)
  players.remove(team1_player1)
  team1_player2 = random.choice(players)
  players.remove(team1_player2)

  # Randomly select two players for team 2
  team2_player1 = random.choice(players)
  players.remove(team2_player1)
  team2_player2 = random.choice(players)
  players.remove(team2_player2)

  # Add the round to the list of rounds
  rounds.append((team1_player1, team1_player2, team2_player1, team2_player2))

  # Add the players back to the pool for the next round
  players.extend([team1_player1, team1_player2, team2_player1, team2_player2])

# Print the rounds
for i, round in enumerate(rounds):
  print(f"Round {i + 1} - ({round[0]} + {round[1]}) vs. ({round[2]} + {round[3]})")
