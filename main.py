import sys


def main():
    print("WELCOME TO THE GAME")
    print("********************************************")
    print("1. Rules")
    print("2. New Game")
    print("3. Resume Game")
    print("4. Quit")
    user_input = input("What would you like to do?")
    if user_input == 1:
        rules()
    elif user_input == 2:
        play_game()
    elif user_input == 3:
        resume_game()
    elif user_input == 4:
        exit_function()

def rules():
    """The rules of the card game called War go here"""
    pass

def play_game():
    """Function to actually run the game - player draws a card, compares to computer, computer determines winner and take appropriate action"""
    pass

def resume_game():
    """Gets the game status from CSV file - should show how many cards each player has and how many cards are left in the deck. Play game as normal from this state."""
    pass

def exit_function():
    print("Thanks for playing!")
    sys.exit()

if __name__ == "__main__":
    main()