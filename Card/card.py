"""A class to represent a playing card"""
#Imports
import random as rn

# constants
suits = ['♠️','♣️','♥️','♦️']
nums = ['2','3','4','5','6','7','8','9','10','11','J','Q','K']

class Constants:
    def __init__(self):
        self.started = 'started'
        self.playing = 'playing'
        self.ended = 'ended'

def to_list(the_string):
    """This function generates a list from the characters of a string"""
    my_list = [each_ch for each_ch in the_string]
    return(mylist)

class Card:
    def __init__(self,num,suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        return str(self.suit) + ' '+ str(self.num)


class Deck:
    """A class representing a deck of cards with only one instance variable 'cards[]' list"""
    def __init__(self):
        self.cards = [Card(each_num,each_suit) for each_suit in suits for each_num in nums]
    
    def __str__(self):
        for each_card in self.cards:
            print(each_card)
        
    
    def shuffle(self):
        """A function to shuffle the cards into an unordered array"""
        for each_card in self.cards:
            random_num = rn.randint(0,len(self.cards)-1)
            random_num2 = rn.randint(0,len(self.cards)-1)
            
            temp = self.cards[random_num] # temporarily store each_card before swapping

            self.cards[random_num] = self.cards[random_num2]
            
            self.cards[random_num2] = temp

    def shuffle2(self):
        i = 0
        while i < len(self.cards):
            random_num = rn.randint(0,len(self.cards)-1)
            temp = self.cards[random_num]
            self.cards[random_num] = self.cards[i]
            self.cards[i] = temp
            i += 1

    def shuffle3(self):
        for i in range(len(self.cards)):
            random_num = rn.randint(0,len(self.cards)-1)
            temp = self.cards[random_num]
            self.cards[random_num] = self.cards[i]
            self.cards[i] = temp
                      
try:  
    my_deck = Deck()
    my_deck.shuffle()
    my_deck.__str__()  # use this instead of print()
    
except TypeError as err:
    print(err)

"""
class Player:
   A class implementing a player for a card game
    def __init__(self,name):
        self.name = name


class LastCard:
    A class implementing the game last card
    contants = Constants()
    def __init__(self,card_per_player,number_of_players):
        self.state = constants.started

lastCard = LastCard()"""
