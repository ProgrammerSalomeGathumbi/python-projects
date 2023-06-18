from deck import Deck
from hand import Hand
from chips import Chips
from blackjack import (
    take_bet, show_some, hit_or_stand, player_busts,
    dealer_busts, player_wins, dealer_wins, push,
    show_all, hit
)

if __name__ == "__main__":

    print("Welcome to Blackjack! Get as close to 21 as you \
          can without going over!\n")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    playing = True

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player exceeds 21, run player_busts() and set playing to False
        if player_hand.value > 21:
            player_busts(player_chips)
            playing = False  # Set playing to False to exit the loop

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    # Inform Player of their chips total
    print("\nPlayer's total chips:", player_chips.total)

    # Ask to play again
    play_again = input("Do you want to play again? Enter 'y' or 'n': ").lower()
    if play_again != 'y':
        play_again = False  # Set play_again to False to exit the loop
