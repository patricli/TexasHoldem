from Deck_module import *
from Player_module import *

#ENV variables
num_players = 2
num_rounds = 40


def play_round(player_list):

    a_Deck = Deck()
    community = []

    #ante
    print("\n")


    # deal two cards to players
    for foo in player_list:
        foo.hand.append(a_Deck.draw_card())
        foo.hand.append(a_Deck.draw_card())

    #betting round 1

    #deal the flop
    community.append(a_Deck.draw_card())
    community.append(a_Deck.draw_card())
    community.append(a_Deck.draw_card())

    #betting round 2

    #deal the turn
    community.append(a_Deck.draw_card())

    #betting round 3

    #deal the river
    community.append(a_Deck.draw_card())

    #round summary
    for foo in player_list:
        print(foo.show_hand())
        print("%s has a bankroll of %d" % (foo.name, foo.bankroll))

    print("\n")
    print("Community cards:")

    print(len(community))
    for bar in community:
        #print(bar.show_card())
        print(bar)

    #clear the table
    for foo in player_list:
        foo.discard_hand()



#create num_players
player_list = []
for i in range(1, num_players+1):
    bar = player("Player %d" % i)
    player_list.append(bar)

for foo in player_list:
    print("%s has a bankroll of %d" % (foo.name, foo.bankroll))

'''
play_round(player_list)
play_round(player_list)
play_round(player_list)
play_round(player_list)
play_round(player_list)

'''


j = 0
while (j < num_rounds):
    play_round(player_list)
    j += 1
    print("Round", j)
