from Deck_module import *
from Player_module import *
from betting import *
from evaluator import *

#ENV variables
num_players = 4
num_rounds = 2
small_blind = 1
big_blind = small_blind * 2

def play_round(player_list):

    a_Deck = Deck()
    community = []
    print("\n")


    # deal two cards to players
    for foo in player_list:
        foo.hand.append(a_Deck.draw_card())
        foo.hand.append(a_Deck.draw_card())

    #betting round 1
    post_small_blind(player_list[0],small_blind)
    post_big_blind(player_list[1], big_blind)
    if len(player_list)>2:
        for i in range(2,len(player_list)):
            act = "call"
            if act.lower() == "call":
                betting_call(player_list[i], big_blind)
            elif act.lower() == "fold":
                betting_fold(player_list[i])
            elif act.lower() == "raise":
                betting_raise(player_list[i])

    #deal the flop
    community.append(a_Deck.draw_card())
    community.append(a_Deck.draw_card())
    community.append(a_Deck.draw_card())

    #evaluate hands
    def eval_rank_hand(board, hand):
        hand_rank = [i.rank for i in hand]
        board_rank = [i.rank for i in board]
    evaluator = Evaluator()
    community_rank = [i.rank for i in community]
    player_hands = []
    for i in player_list:
            hand_rank = [ card.rank for card in i.hand]
            player_hands.append(evaluator.evaluate(community_rank, hand_rank))
    print("After the flop:")
    print(player_hands)
    print("\n")

    #betting round 2
    if len(player_list)>2:
        for foo in player_list:
            act = "call"
            if act.lower() == "call":
                betting_call(foo, big_blind)
            elif act.lower() == "fold":
                betting_fold(foo)
            elif act.lower() == "raise":
                betting_raise(foo)



    #deal the turn
    community.append(a_Deck.draw_card())

    #evaluate hands
    def eval_rank_hand(board, hand):
        hand_rank = [i.rank for i in hand]
        board_rank = [i.rank for i in board]
    evaluator = Evaluator()
    community_rank = [i.rank for i in community]
    player_hands = []
    for i in player_list:
            hand_rank = [ card.rank for card in i.hand]
            player_hands.append(evaluator.evaluate(community_rank, hand_rank))
    print("After the turn:")
    print(player_hands)
    print("\n")

    #betting round 3



    #deal the river
    community.append(a_Deck.draw_card())

    #evaluate hands
    def eval_rank_hand(board, hand):
        hand_rank = [i.rank for i in hand]
        board_rank = [i.rank for i in board]
    evaluator = Evaluator()
    community_rank = [i.rank for i in community]
    player_hands = []
    for i in player_list:
            hand_rank = [ card.rank for card in i.hand]
            player_hands.append(evaluator.evaluate(community_rank, hand_rank))
    print("After the river:")
    print(player_hands)
    print("\n")

    #betting before reveal

    #round summary
    for foo in player_list:
        #print(foo)
        print(foo.show_hand())
        print("%s has a bankroll of %d" % (foo.name, foo.bankroll))

    win_hand = max(player_hands)
    win_index = player_hands.index(win_hand)
    print(player_list[win_index].name + "wins with hand of")
    win_rank = [i.rank for i in player_list[win_index].hand]
    win_cards = [i.show_card() for i in player_list[win_index].hand] + [i.show_card() for i in community]
    print(win_cards)
    evaluator.hand_summary(community_rank, [win_rank])

    print("\n")
    print("Community cards:")

    #print(len(community))
    for bar in community:
        print(bar.show_card())
        #print(bar)

    #clear the table
    for foo in player_list:
        foo.discard_hand()



#------------->>Main<<--------------

#create num_players
player_list = []
for i in range(1, num_players+1):
    bar = player("Player %d" % i)
    player_list.append(bar)

for foo in player_list:
    print("%s has a bankroll of %d" % (foo.name, foo.bankroll))


j = 1
deal_order = player_list

while (j <= num_rounds):

    print("Round", j)
    play_round(deal_order)

    #rotate dealer order
    new_order = deal_order[1:]
    new_order.append(deal_order[0])
    deal_order = new_order
    #print("Player deal order", deal_order)

    j += 1
