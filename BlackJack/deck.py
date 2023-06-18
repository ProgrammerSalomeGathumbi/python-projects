#!/usr/bin/python3
"""
Deck Module
"""
import random
from card import Card


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six',
                 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
                 'Queen', 'King', 'Ace')

        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_str = ""
        for card in self.deck:
            deck_str += str(card) + "\n"
        return deck_str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
