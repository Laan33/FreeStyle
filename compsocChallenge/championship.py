import importlib
import os

"""
    All the algorithms are in the submissions folder.
    The naming format is <team_name>.py
    
    Load all the algorithms from the submissions folder, and create a tournament tree.
    It will be a knockout tournament, where the winner of each round advances to the next round.
    
    
    In the play functions, the algorithm should return 'rock', 'paper', or 'scissors'.
    We pass the opponents move from the previous game to the play function of each algorithm.
    If it's the first game, the last_opponent_move will be None.
    
    The algorithm returns it's move for the current game.
    
    In each round, the algorithms play against each other 20 times.
"""

def load_algorithms():
    """
    Load all the algorithms from the submissions folder.
    """
    algorithms = []
    for file in os.listdir("submissions"):
        if file.endswith(".py"):
            team_name = file.split(".")[0]
            module = importlib.import_module(f"submissions.{team_name}")
            algorithms.append(module)
    return algorithms

# Tournament knockout tree
def play_tournament():
    """
    Tournament knockout tree.
    """
    algorithms = load_algorithms()
    while len(algorithms) > 1:
        winners = []
        for i in range(0, len(algorithms), 2):
            algorithm_1 = algorithms[i].RockPaperScissors()
            algorithm_2 = algorithms[i + 1].RockPaperScissors()
            score = play_round(algorithm_1, algorithm_2)
            if score > 0:
                winners.append(algorithms[i])
            else:
                winners.append(algorithms[i + 1])
        algorithms = winners
    return algorithms[0].RockPaperScissors()



def play_round(algorithm_1, algorithm_2):
    """
    Play 20 games between two algorithms.
    """
    score = 0
    for _ in range(20):
        move_1 = algorithm_1.play(algorithm_2.last_move)
        move_2 = algorithm_2.play(algorithm_1.last_move)
        algorithm_1.last_move = move_2
        algorithm_2.last_move = move_1
        score += base_game_rules(move_1, move_2)
    return score


# Simple function to define rock paper scissors rules
def base_game_rules(move1, move2):
    if move1 == move2:
        return 0
    if move1 == 'rock':
        return 1 if move2 == 'scissors' else -1
    if move1 == 'paper':
        return 1 if move2 == 'rock' else -1
    if move1 == 'scissors':
        return 1 if move2 == 'paper' else -1
    return 0

