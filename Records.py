from Account import get_balance

user_wins = 0
dealer_wins = 0


def stats(winner):
    global user_wins, dealer_wins

    if winner == "u":
        user_wins += 1
    else:
        dealer_wins += 1


def get_games():
    global user_wins, dealer_wins
    return user_wins + dealer_wins


def get_stats():
    global user_wins, dealer_wins
    games_played = user_wins + dealer_wins
    if games_played > 0:
        win_percentage = round((user_wins/games_played)*100)
        print("\n\n\n\nGame Statistics\n\nGames played: "+str(games_played) +
              "\nGames Won: " + str(user_wins) + "\nWin Percentage: " + str(win_percentage)+"%")
        print("Your Balance is: " + str(get_balance()))
        if get_balance() > 1000:
            print("You made " + str(get_balance() - 1000) + "$!")
