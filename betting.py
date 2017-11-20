from Player_module import *

def post_small_blind(player, small_blind):
    player.bankroll -= small_blind
    player.active = 1
    return 0

def post_big_blind(player, big_blind):
    player.bankroll -= big_blind
    player.active = 1
    return 0

def betting_call(player, big_blind):
    player.bankroll -= big_blind
    player.active = 1
    return 0

def betting_fold(player):
    player.active = 0
    return 0

def betting_raise(player, big_blind):
    player.bankroll -= big_blind
    player.active = 1
    return 0