import random


def create_deck():
    """
    :return: An array list containing 52 element to represent each card in a deck
    """
    nums, deck = [], []
    for i in range(2, 11):
        nums.append(i)
    face = ["Jack", "Queen", "King", "Ace"]
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    nums.extend(face)

    for i in suits:
        for j in nums:
            deck.append(str(j) + " of " + i)
    return deck


def shuffle(deck):
    """
    :param deck: An array list containing 52 element to represent each card in a deck
    :return: The same array list with its elements shuffled
    """
    shuffled = []
    rands = []
    for e in range(52):
        rands.append(e)

    for k in range(52):
        num = random.randint(0, len(rands)-1)
        shuffled.append(deck[num])
        rands.remove(rands[num])
        deck.remove(deck[num])
    return shuffled


def new_hand(dealer, playing_cards):
    """

    :param dealer:
    :param playing_cards:
    :return:
    """
    tot = calc(dealer, user=False)
    while tot < 17:
        hit_dealer(playing_cards, dealer)
        tot = calc(dealer, user=False)
    # time.sleep(5)


def calc(player, user):
    """

    :param player:
    :param user:
    :return:
    """
    count = 0
    for i in range(len(player)):
        val = player[i].split()[0]
        if val == "Jack"or val == "Queen" or val == "King":
            val = 10
        elif val == "Ace":
            if user:
                set_val = input("Do you want the Ace to be a 1 or a 11? ")
                while set_val.strip() != "1" and set_val.strip() != "11":
                    set_val = input("Make Ace a 1 or a 11: ")
                val = set_val
            else:
                val = 11
                temp = count + val
                if temp > 21:
                    val = 1

        count = int(val) + count
    return count


def hit_dealer(playing_cards, dealer_hand):
    """
    Adds a card to the dealers hand
    """
    dealer_hand.append(playing_cards[0])
    playing_cards.pop(0)


def hit_user(playing_cards, user_hand):
    """
    Adds a card to the users hand
    """
    user_hand.append(playing_cards[0])
    playing_cards.pop(0)
