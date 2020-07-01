
from Records import stats, get_stats, get_games
import time
from CardCreator import user_image, dealer_image
from Account import set_bet, lose, win, get_balance
from Deck import create_deck, shuffle, calc, new_hand, hit_user, hit_dealer

loser = False
playing_cards = create_deck()
play = input("Welcome to the casino, how about some black jack\n\t (yes or no): ")
while play.strip().lower() == "yes":
    user_hand = []
    dealer_hand = []

    if get_games() == 0 or len(playing_cards) < 10:
        print("\nShuffling deck", end=" ")
        time.sleep(.2)
        print(".", end=" ")
        time.sleep(.10)
        print(".", end=" ")
        time.sleep(.5)
        print(".", end=" ")
        time.sleep(.5)
        print(".", end=" ")

        playing_cards = shuffle(create_deck())

    while play.strip().lower() == "yes":
        bet = input("\nHow much would you like to bet? (Your balance is " + str(get_balance()) + "$): ")
        set_bet(bet)
        hit_user(playing_cards, user_hand)
        hit_user(playing_cards, user_hand)
        hit_dealer(playing_cards, dealer_hand)
        hit_dealer(playing_cards, dealer_hand)

        print("\n\nYour hand is: ")
        time.sleep(.5)
        user_image(user_hand)
        total = calc(user_hand, user=True)
        print("\nYour total is: " + str(total))
        print("\nDealers hand is:")
        time.sleep(.5)
        dealer_image(dealer_hand, False)
        hit = input("\nhit or stay: ")
        while hit.strip().lower() == "hit":
            if hit.strip().lower() == "hit":
                hit_user(playing_cards, user_hand)
            print("\nYour new hand is")
            time.sleep(.5)
            user_image(user_hand)
            total = calc(user_hand, user=True)
            print("\nYour total is: " + str(total))
            if total > 21:
                print("\nYou lose!")
                loser = lose()
                stats("d")
                if lose:
                    break
                break
            hit = input("\nhit or stay: ")
        if total > 21:
            break
        new_hand(dealer_hand, playing_cards)
        d_total = calc(dealer_hand, user=False)
        print("\nDealers hand is:")
        time.sleep(.5)
        dealer_image(dealer_hand, True)
        print("\nDealer total is: " + str(d_total))
        if d_total > 21:
            print("you win!")
            win()
            stats("u")
            break
        if d_total > total:
            print("You lose!")
            loser = lose()
            stats("d")
            break
        else:
            print("you win!")
            win()
            stats("u")
            break
    if loser:
        break
    play = input("\nKeep playing?\n\t (yes or no): ")

get_stats()
