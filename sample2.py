
class Card():
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

class Deck:
    def __init__(self):
        self.data = []
        Suits = ["Spade", "Heart", "Club", "Diamond"]

        for suit in Suits:
            for i in range(1,14):
                a = Card(suit, i)
                #print(a.suit)
                #print(a.num)
                self.data.append(a)

    def remainder(self):
        count = 0
        for i in self.data:
            count = count+1
        return count


a_Deck = Deck()
print(a_Deck.remainder())

