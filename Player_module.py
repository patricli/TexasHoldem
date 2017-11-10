from Deck_module import*

class player():

    def __init__(self, name):

        self.name = name
        self.bankroll = 5000
        self.hand = []


    def show_hand(self):
        if len(self.hand)<2:
            return "Incomplete hand"
        else:
            #return ("%s has %s and %s" % (self.name, self.hand[0].show_card(), self.hand[1].show_card()))
            str = "Player has " + self.hand[0].show_card() + " and " + self.hand[1].show_card()
            return str

            #return "Player has " + self.hand[0].show_card() + " and " + self.hand[1].show_card()

    def discard_hand(self):
        self.hand = []

