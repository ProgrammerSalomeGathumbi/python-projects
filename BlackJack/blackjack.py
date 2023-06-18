#!/usr/bin/python3
"""
The main BlackJack Script
"""
import random
from card import Card
from deck import Deck
from hand import Hand
from chips import Chips

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


def take_bet(chips):
    """A function for taking bets """
    while True:
        try:
            chips.bet = int(input("Place your bet: "))
            if chips.bet > chips.total:
                print("Insufficient chips. Please enter a valid bet.")
                continue
            break
        except ValueError:
            print("Invalid bet. Please enter a valid bet.")


def hit(deck, hand):
    """A function for taking hits """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """A function prompting player  to hit or standd"""
    global playing
    while True:
        choice = input("Do you want to Hit or Stand? \
                       Enter 'h' or 's': ").lower()
        if choice == 'h':
            hit(deck, hand)
        elif choice == 's':
            print("Player stands. Dealer's turn.")
            playing = False
        else:
            print("Invalid input. Please enter 'h' or 's'.")
            continue
        break


def show_some(player, dealer):
    """A function to display cards """
    print("\nDealer's Hand:")
    print("<card hidden>")
    print(dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n')


def show_all(player, dealer):
    """Displays Cards """
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand Value =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("Player's Hand Value =", player.value)


def player_busts(chips):
    """Handles  end of game via player loss """
    print("Player busts!")
    chips.lose_bet()


def player_wins(chips):
    """Handles end of game via a player win"""
    print("Player wins!")
    chips.win_bet()


def dealer_busts(chips):
    """Handles end of games via dealer loss and player win """
    print("Dealer busts! Player wins!")
    chips.win_bet()


def dealer_wins(chips):
    """Handles end of games via dealer win and player loss """
    print("Dealer wins! Player loses!")
    chips.lose_bet()


def push():
    """Shows a tie """
    print("It's a tie! Push.")
