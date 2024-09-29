# You must rename this file to 'team<team_number>.py' before submitting.

# Members: <team members>

class RockPaperScissors:
    def __init__(self):
        self.last_move = None
        self.team_name = "<team name>"

    def play(self, last_opponent_move):
        """
        Implement your algorithm here.
        This function should return 'rock', 'paper', or 'scissors'.
        The opponents last move for the previous game is an input to this function.
        """
        move = 'rock'  # Example move
        self.last_move = move
        return move  # Example return value

# Example usage
# rps = RockPaperScissors()
# print(rps.play(None))  # First move
# print(rps.play('scissors'))  # Next move
