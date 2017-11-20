#from Deck_module import Card

"""
Static class that handles cards. We represent cards as 32-bit integers, so
there is no object instantiation - they are just ints. Most of the bits are
used, and have a specific meaning. See below:

                                Card:

                      bitrank     suit rank   prime
                +--------+--------+--------+--------+
                |xxxbbbbb|bbbbbbbb|cdhsrrrr|xxpppppp|
                +--------+--------+--------+--------+

    1) p = prime number of rank (deuce=2,trey=3,four=5,...,ace=41)
    2) r = rank of card (deuce=0,trey=1,four=2,five=3,...,ace=12)
    3) cdhs = suit of card (bit turned on based on suit of card)
    4) b = bit turned on depending on rank of card
    5) x = unused

This representation will allow us to do very important things like:
- Make a unique prime prodcut for each hand
- Detect flushes
- Detect straights

and is also quite performant.
"""

# initialize deck as a list of 52 cards with suit from 0-3, and num from 1-13
#suit_list = ["Diamond", "Club", "Heart", "Spade"]

# the basics
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
SUIT_RANKS = {
    3 : 1,  # spades
    2 : 2,  # hearts
    1 : 4,  # diamonds
    0 : 8,  # clubs
}

'''
def rank_card(card):
    """
    Converts Card string to binary integer representation of card, inspired by:

    http://www.suffecool.net/poker/evaluator.html
    """

    rank_int = card.num - 2
    suit_int = SUIT_RANKS[card.suit]
    rank_prime = PRIMES[rank_int]


    bitrank = 1 << rank_int << 16
    suit = suit_int << 12
    rank = rank_int << 8

    return bitrank | suit | rank | rank_prime
'''


def prime_product_from_hand(card):
    """
    Expects a list of cards in integer form.
    """
    product = 1
    for c in card:
        product *= (c & 0xFF)

    return product


def prime_product_from_rankbits(rankbits):
    """
    Returns the prime product using the bitrank (b)
    bits of the hand. Each 1 in the sequence is converted
    to the correct prime and multiplied in.

    Params:
        rankbits = a single 32-bit (only 13-bits set) integer representing
                the ranks of 5 _different_ ranked cards
                (5 of 13 bits are set)

    Primarily used for evaulating flushes and straights,
    two occasions where we know the ranks are *ALL* different.

    Assumes that the input is in form (set bits):

                          rankbits
                    +--------+--------+
                    |xxxbbbbb|bbbbbbbb|
                    +--------+--------+

    """
    product = 1
    for i in range(13):
        # if the ith bit is set
        if rankbits & (1 << i):
            product *= PRIMES[i]

    return product


