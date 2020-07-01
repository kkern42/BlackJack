balance = 1000
bet = 0


def set_bet(amount):
    """

    :param amount:
    :return:
    """
    global bet
    amount = int(amount)
    if amount <= balance:
        bet = amount
    else:
        print("You do not have enough to bet " + str(amount) + ".\n Current balance is: " + str(get_balance()))
        new_bet = int(input("Enter an amount you can afford."))
        while new_bet > balance:
            new_bet = int(input("Enter an amount you can afford: "))
        bet = new_bet


def lose():
    """

    :return:
    """
    global balance, bet
    balance = balance - bet
    if balance == 0:
        return True


def win():
    """

    :return:
    """
    global balance, bet
    balance = balance + bet


def get_balance():
    """

    :return:
    """
    return balance
