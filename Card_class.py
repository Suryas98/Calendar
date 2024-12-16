# Card class

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

two_hearts = Card("Hearts","Two")
three_of_clubs = Card("Clubs",'Three') 
print(two_hearts)            # It print the heart value
print(two_hearts.suit)       # It define the suit of hearts
print(two_hearts.rank)       # It define the rank of hearts
print(two_hearts.value)      # It print the value of heart in numbers
print(three_of_clubs.value)  # It define the value of clubs
print(two_hearts.value < three_of_clubs.value)  # It define less than or not
print(two_hearts.value > three_of_clubs.value)  # It define greater than or not
print(two_hearts.value == three_of_clubs.value) # It define equal or not

