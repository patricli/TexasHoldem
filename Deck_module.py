import random

class Card():   #an object for cards with value suit and num
    def show_card(self):    #returns card in human readable format
        suit_list = ["Diamond","Club","Heart","Spade"]
        if (self.num == 14):
            return "Ace of " + suit_list[self.suit]
        elif (self.num == 11):
            return "Jack of " + suit_list[self.suit]
        elif (self.num == 12):
            return "Queen of " + suit_list[self.suit]
        elif (self.num == 13):
            return "King of " + suit_list[self.suit]
        else:
            return str(self.num) + " of " + suit_list[self.suit]



    def _rank_card(card):
        """
        Converts Card string to binary integer representation of card, inspired by:

        http://www.suffecool.net/poker/evaluator.html
        """

        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        SUIT_RANKS = {
            3: 1,  # spades
            2: 2,  # hearts
            1: 4,  # diamonds
            0: 8,  # clubs
        }

        rank_int = card.num - 2
        suit_int = SUIT_RANKS[card.suit]
        rank_prime = PRIMES[rank_int]

        bitrank = 1 << rank_int << 16
        suit = suit_int << 12
        rank = rank_int << 8

        return bitrank | suit | rank | rank_prime

    def __init__(self, num, suit):

        self.num = num    #int from 1-13
        self.suit = suit  # int from 0-3
        self.rank = self._rank_card()  # dec int rank

class Deck:
    #initialize deck as a list of 52 cards with suit from 0-3, and num from 1-13
    def __init__(self): #initialize
        self.data = []

        #Suits = ["Spade", "Heart", "Club", "Diamond"]

        for suit in range(0,4):
            for i in range(2,15):  #Ace=14
                a = Card(i, suit)
                self.data.append(a)

    #generate a random int and pop that index position from the deck
    def draw_card(self):
        if self.deck_len()>0:
            index = random.randint(0, self.deck_len() - 1)
            #print("Random index = ", index)  # temp check
            return self.data.pop(index)
        else:
            return ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Empty deck"

    def deck_len(self):
        return len(self.data)

#validation tests

