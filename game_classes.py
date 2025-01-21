# This file is going to contain all the classes needed to play the game
# Game, Deck, Card, and Hand classes

import random 

class Card:
    """Represents a single playing card"""
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    SUITS = ["Clubs", "Spades", "Hearts", "Diamonds"]
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.RANKS.index(rank) #since cards starts at 2 but index starts at 0; Ace is worth 14
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """Represents the entire 52 card deck"""
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_one(self):
        """Deals one card from the deck"""
        return self.cards.pop() if self.cards else None
    
    def __len__(self):
        return len(self.cards)

class Hand:
    """Represents the cards owned by each player"""
    def __init__(self):
        self.cards = []
    
    def add_cards(self, new_cards):
        """Add new card(s) to the hand"""
        if isinstance(new_cards, list):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def play_card(self):
        """Plays (removes and returns) top card from the hand; return None if no cards in hand"""
        if self.cards: 
            return self.cards.pop(0)
        return None
    
    def has_cards(self):
        """Checks if player has cards in hand"""
        return len(self.cards) > 0
    
    def __repr__(self):
        return f"Player has {len(self.cards)} cards remaining."
    
    def __len__(self):
        return len(self.cards)

class Game:
    """Represents the state of the game and runs the gameplay"""
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.computer_hand = Hand()
        self.initialize_hands()
    
    def initialize_hands(self):
        """Distributes cards evenly to both players"""
        while len(self.deck) > 0:
            self.player_hand.add_cards(self.deck.deal_one())
            self.computer_hand.add_cards(self.deck.deal_one())

    def play_round(self):
        """A single round of War"""
    
        player_card = self.player_hand.play_card()
        computer_card = self.computer_hand.play_card()
        if player_card is None or computer_card is None:
            self.is_game_over()
            return
        print(f"Player plays {player_card}. \n Computer plays {computer_card}.")
        

        if player_card.value > computer_card.value:
            self.player_hand.add_cards([player_card, computer_card])
            print("Player wins the round")
        elif player_card.value < computer_card.value:
            self.computer_hand.add_cards([player_card, computer_card])
            print("Computer wins this round")
        else:
            print("It's a tie! Starting a battle...")
            self.resolve_war(player_card, computer_card)
        
        if self.is_game_over():
            input("Game over! Press any key to return to the menu.")
            return
        else:
            self.play_round()

    def resolve_war(self, player_card, computer_card, card_pile=[]):
        """Each player adds a card to the pile, then plays the next card. Winner of battle takes whole pile. If either player runs out of cards, they 
        immediately lose the game."""
        card_pile.extend([player_card, computer_card])
        if self.player_hand.has_cards():
            card_pile.append(self.player_hand.play_card())
        else:
            if self.is_game_over():
                return
        if self.computer_hand.has_cards():
            card_pile.append(self.computer_hand.play_card())
        else:
            if self.is_game_over():
                return
        player_card = self.player_hand.play_card()
        computer_card = self.computer_hand.play_card()
        print(f"Player plays {player_card}. \n Computer plays {computer_card}.")
        if player_card.value > computer_card.value:
            card_pile.extend([player_card, computer_card])
            self.player_hand.add_cards(card_pile)
            print("Player wins the round")
        elif player_card.value < computer_card.value:
            card_pile.extend([player_card, computer_card])
            self.computer_hand.add_cards(card_pile)
            print("Computer wins this round")
        else:
            print("It's a tie! Starting a battle...")
            self.resolve_war(player_card, computer_card, card_pile)


    def is_game_over(self):
        if not self.player_hand.has_cards() or not self.computer_hand.has_cards():
            if self.player_hand.has_cards and not self.computer_hand.has_cards():
                print("Player Wins! Congratulations!")
            elif not self.computer_hand.has_cards() and self.computer_hand.has_cards():
                print("Computer Wins. Better luck next time!")
            else:
                print("It's a tie! You're both out of cards.")
            return True
        return False
    
    def __repr__(self):
        return (f"{self.player_hand} \n {self.computer_hand}")
    