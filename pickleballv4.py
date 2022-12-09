import random

# Players in the pool
players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11", "Player 12"]

# Set of players that each player has played with in previous rounds
player_teammates = {player: set() for player in players}

# List of rounds
rounds = []

# Number of rounds to play
num_rounds = 10

# Play the rounds
for i in range(num_rounds):
  # Set the players for team 2 to None initially
  team2_player1 = None
  team2_player2 = None

  # Randomly select two players for team 1
  team1_player1 = random.choice(players)
  team1_player2 = random.choice(players)
  while team1_player2 in player_teammates[team1_player1] or team1_player2 in (team1_player1, team2_player1, team2_player2):
    team1_player2 = random.choice(players)

  # Randomly select two players for team 2
  team2_player1 = random.choice(players)
  team2_player2 = random.choice(players)
  while team2_player2 in player_teammates[team2_player1] or team2_player2 in (team1_player1, team1_player2, team2_player1):
    team2_player2 = random.choice(players)

  # Add the round to the list of rounds
  rounds.append((team1_player1, team1_player2, team2_player1, team2_player2))

  # Update the set of players that each player has played with in previous rounds
  player_teammates[team1_player1].add(team1_player2)
  player_teammates[team1_player2].add(team1_player1)
  player_teammates[team2_player1].add(team2_player2)
  player_teammates[team2_player2].add(team2_player1)

# Print the rounds
for i, round in enumerate(rounds):
  print(f"Round {i + 1} - ({round[0]} + {round[1]}) vs. ({round[2]} + {round[3]})")
