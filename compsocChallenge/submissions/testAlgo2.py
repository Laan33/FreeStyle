# You must rename this file to 'team<team_number>.py' before submitting.

# Members: <team members>
import random

class RockPaperScissors:
    def __init__(self):
        self.last_move = None
        self.team_name = "Cathal"

    def play(self, yourMovesArray, opponentsMovesArray):
        """
        Implement your algorithm here.
        This function should return 'rock', 'paper', or 'scissors'. No uppercase letters.
        There are two arrays that you can use to read the previous moves and results.

        Example arrays with previous moves
        Your moves: ['rock', 'paper', 'scissors']
        Opponent's moves: ['scissors', 'rock', 'paper']

        Best of luck!
        """


        move = 'scissors'
        return move




# Example usage
# rps = RockPaperScissors()
# print(rps.play(None))  # First move
# print(rps.play('scissors'))  # Next move
