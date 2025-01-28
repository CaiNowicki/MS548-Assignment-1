import sys
import time
import os
from game_classes import Game

def main():
    menu()

def menu():
    clear_terminal()
    print("WELCOME TO THE GAME")
    print("********************************************")
    print("1. Rules")
    print("2. New Game")
    print("3. Resume Game")
    print("4. Quit")
    user_input = input("What would you like to do?")
    try:
        user_input = int(user_input)
        if user_input == 1:
            rules()
        elif user_input == 2:
            play_game()
        elif user_input == 3:
            resume_game()
        elif user_input == 4:
            exit_function()
        else:
            print("Invalid selection. Please enter a numeric value between 1 and 4.")
            menu()
    except ValueError:
        "Invalid selection. Please enter a numeric value between 1 and 4."
        print()
def clear_terminal():
    """Clears the terminal screen when called"""
    os.system('cls' if os.name == 'nt' else 'clear')

def rules():
    clear_terminal()
    """The rules of the card game called War go here"""
    print("War (aka Battle) is a simple card game.")
    print("The cards are distributed evenly to the players, without revealing any of the cards to either player.")
    print("""Each round consists of players comparing the top card of their stack. The player with the higher ranked card takes both 
          cards and adds them to the bottom of their stack. In the event of a tie, the players continue drawing cards until one is higher; the winning player takes 
          all of the cards from the multiple battles.""")
    print("The objective of the game is to collect all of the cards!")
    time.sleep(1)
    input("Press any key to return to the menu.")
    menu()
    
    menu()

def play_game():
    clear_terminal()
    """Function to actually run the game - player draws a card, compares to computer, computer determines winner and take appropriate action"""
    print("Starting a new game...")
    time.sleep(1)
    
    # Create a Game instance
    game = Game()
    
    # Begin the game loop
    while not game.is_game_over():
        game.play_round()
    
    # After game completion, return to the main menu
    input("Game over! Press any key to return to the menu.")
    menu()

def resume_game():
    clear_terminal()
    """Gets the game status from CSV file - should show how many cards each player has and how many cards are left in the deck. Play game as normal from this state."""
    print("Save function not yet implemented. Sorry!")
    menu()

def exit_function():
    print("Thanks for playing!")
    time.sleep(1)
    sys.exit()

if __name__ == "__main__":
    main()