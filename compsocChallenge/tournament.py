import importlib
import os

"""
    All the algorithms are in the submissions folder.
    The naming format is <team_name>.py
    
    Load all the algorithms from the submissions folder, and create a tournament tree.
    It will be a knockout tournament, where the winner of each round advances to the next round.
    
    
    In the play functions, the algorithm should return 'rock', 'paper', or 'scissors'.
    In each round, we track the moves in two arrays, and provide each to the algorithms.
    Each array has the move of an algorithm.
    
    The algorithm returns it's move for the current game.
    
    In each round, the algorithms play against each other 20 times.
"""

def load_algorithms():
    """
    Load all the algorithms from the submissions folder.
    """
    algorithms = []
    for file in os.listdir("submissions"):
        if file.endswith(".py") and file.startswith("team"):
            team_name = file.split(".")[0]
            module = importlib.import_module(f"submissions.{team_name}")
            algorithms.append(module)
    # Print the names from the RockPaperScissors class instances.
    print([module.RockPaperScissors().team_name for module in algorithms])
    return algorithms

def play_tournament():
    """
    Tournament knockout tree.
    """
    algorithms = load_algorithms()
    stage = 1
    while len(algorithms) > 1:
        winners = []
        losers = []

        # If there is an odd number of algorithms, select a losing algorithm to play against the last algorithm
        if len(algorithms) % 2 == 1:
            last_algorithm = algorithms[-1]
            algorithms = algorithms[:-1]
            algorithm_1 = last_algorithm.RockPaperScissors()
            algorithm_2 = algorithms[-1].RockPaperScissors()
            score = play_round(algorithm_1, algorithm_2)
            if score > 0:
                winners.append(last_algorithm)
                losers.append(algorithms[-1])
            else:
                winners.append(algorithms[-1])
                losers.append(last_algorithm)
            algorithms = algorithms[:-1]

        for i in range(0, len(algorithms), 2):
            algorithm_1 = algorithms[i].RockPaperScissors()
            algorithm_2 = algorithms[i + 1].RockPaperScissors()
            score = play_round(algorithm_1, algorithm_2)
            if score > 0:
                winners.append(algorithms[i])
                losers.append(algorithms[i + 1])
            else:
                winners.append(algorithms[i + 1])
                losers.append(algorithms[i])
        algorithms = winners
        print(f"Stage {stage} winners: {[algorithm.__name__ for algorithm in algorithms]}")
        stage += 1

    return algorithms[0].RockPaperScissors()



def play_round(algorithm_1, algorithm_2):
    """
    Play 20 games between two algorithms.
    Two arrays are used to track the moves of the algorithms.
    """
    moves_1 = []
    moves_2 = []
    score = 0
    tiebreaker_count = 0

    for _ in range(20):
        move_1 = algorithm_1.play(moves_1, moves_2)
        move_2 = algorithm_2.play(moves_2, moves_1)

        moves_1.append(move_1)
        moves_2.append(move_2)
        print(f"Algorithm 1: {move_1}, Algorithm 2: {move_2}, Score: {score}")
        score += base_game_rules(move_1, move_2)

    if score == 0:
        print("Tie breaker!")

    # if it is a tiebreaker, keep playing until there is a winner
    while score == 0:
        tiebreaker_count += 1
        print(f"Playing tiebreaker {tiebreaker_count}!")
        move_1 = algorithm_1.play(moves_1, moves_2)
        move_2 = algorithm_2.play(moves_2, moves_1)

        moves_1.append(move_1)
        moves_2.append(move_2)

        score += base_game_rules(move_1, move_2)
        print(f"Score: {score}")

        if tiebreaker_count > 0:
            print("Tiebreaker limit reached")
            break

    return score


# Simple function to define rock paper scissors rules
def base_game_rules(move1, move2):
    # Validate moves
    if move1 not in ['rock', 'paper', 'scissors'] or move2 not in ['rock', 'paper', 'scissors']:
        raise ValueError("Invalid move")

    if move1 == move2:
        return 0
    if move1 == 'rock':
        return 1 if move2 == 'scissors' else -1
    if move1 == 'paper':
        return 1 if move2 == 'rock' else -1
    if move1 == 'scissors':
        return 1 if move2 == 'paper' else -1
    return 0

if __name__ == "__main__":
    winner = play_tournament()
    print(f"The overall winner is: {winner.team_name}")