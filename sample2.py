import random


class Card():
    def __init__(self, suit, num):

        self.suit = suit
        self.num = num

    def show_card(self):
        suit_list = ["Diamond","Club","Heart","Spade"]
        if (self.num == 1):
            return "Ace of " + suit_list[self.suit]
        elif (self.num == 11):
            return "Jack of " + suit_list[self.suit]
        elif (self.num == 12):
            return "Queen of " + suit_list[self.suit]
        elif (self.num == 13):
            return "King of " + suit_list[self.suit]
        else:
            return str(self.num) + " of " + suit_list[self.suit]

class Deck:
    def __init__(self):
        self.data = []

        #Suits = ["Spade", "Heart", "Club", "Diamond"]

        for suit in range(0,4):
            for i in range(1,14):
                a = Card(suit, i)
                #print(a.suit)
                #print(a.num)
                self.data.append(a)
        self.len = len(self.data)

    def remainder(self):
        count = 0
        for i in self.data:
            count = count+1
        return count

    def draw_card(self):
        index = random.randint(0,self.len-1)
        print("Random index = " + str(index))
        return self.data.pop(index)


a_Deck = Deck()
print(a_Deck.remainder())
print(a_Deck.len)
print(a_Deck.draw_card().show_card())
