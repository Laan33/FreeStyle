"""
Only this file needs to be submitted. The other files are for reference only.
BEFORE submitting, you must:
    - rename this file to 'team<team_number>.py'
    - make a good team name
    - test your algorithm actually works by running the tests below

i.e. if your team number is 1, rename this file to 'team1.py'.
"""



# Members: <team members>

class RockPaperScissors:
    def __init__(self):
        self.last_move = None
        self.team_name = "<team name>" # You can give this a name of your choice

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

        # Example move
        move = 'rock'
        return move


"""
    This is a simple test to check that the algorithm returns a valid moves.
"""
if __name__ == "__main__":
    rps = RockPaperScissors()
    try:
        # Test the first move
        first_move = rps.play([], [])
        assert first_move in ['rock', 'paper', 'scissors'], "Invalid move returned"

        # Test subsequent moves
        moves = ['rock', 'paper', 'scissors']
        for move in moves:
            next_move = rps.play([move], [move])
            assert next_move in ['rock', 'paper', 'scissors'], "Invalid move returned"

        print("All tests passed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
