
def user_image(hand):
    """

    :param hand:
    :return:
    """
    count = 1
    for i in hand:
        if count != len(hand):
            print("-----------", end=" ")
            count += 1
        else:
            print("-----------")
    count = 1
    for i in hand:
        num = i.split()[0][0]
        if count != len(hand):
            if num == "1":
                num = num + "0"
                print("|" + num + "       |", end=" ")
            else:
                print("|" + num + "        |", end=" ")
            count += 1
        else:
            if num == "1":
                num = num + "0"
                print("|" + num + "       |")
            else:
                print("|" + num + "        |")
    count = 1
    for i in hand:
        face = i.split()[2][0]
        if count != len(hand):
            print("|    " + face + "    |", end=" ")
            count += 1
        else:
            print("|    " + face + "    |")
    count = 1
    for i in hand:
        num = i.split()[0][0]
        if count != len(hand):
            if num == "1":
                num = num + "0"
                print("|       " + num + "|", end=" ")
            else:
                print("|        " + num + "|", end=" ")
            count += 1
        else:
            if num == "1":
                num = num + "0"
                print("|       " + num + "|")
            else:
                print("|        " + num + "|")
    count = 1
    for i in hand:
        if count != len(hand):
            print("-----------", end=" ")
            count += 1
        else:
            print("-----------")


def dealer_image(hand, hit):
    if not hit:
        count = 1
        for i in hand:
            if count == 1:
                print("-----------", end=" ")
                count += 1
            else:
                print("-----------")
        count = 1
        for i in hand:
            num = i.split()[0][0]
            if count == 1:
                if num == "1":
                    num = num + "0"
                    print("|" + num + "       |", end=" ")
                else:
                    print("|" + num + "        |", end=" ")
                count += 1
            else:
                print("|         |")
        count = 1
        for i in hand:
            face = i.split()[2][0]
            if count == 1:
                print("|    " + face + "    |", end=" ")
                count += 1
            else:
                print("|         |")
        count = 1
        for i in hand:
            num = i.split()[0][0]
            if count == 1:
                if num == "1":
                    num = num + "0"
                    print("|       " + num + "|", end=" ")
                else:
                    print("|        " + num + "|", end=" ")
                count += 1
            else:
                print("|         |")
        count = 1
        for i in hand:
            if count == 1:
                print("-----------", end=" ")
                count += 1
            else:
                print("-----------")
    else:
        count = 1
        for i in hand:
            if count != len(hand):
                print("-----------", end=" ")
                count += 1
            else:
                print("-----------")
        count = 1
        for i in hand:
            num = i.split()[0][0]
            if count != len(hand):
                if num == "1":
                    num = num + "0"
                    print("|" + num + "       |", end=" ")
                else:
                    print("|" + num + "        |", end=" ")
                count += 1
            else:
                if num == "1":
                    num = num + "0"
                    print("|" + num + "       |")
                else:
                    print("|" + num + "        |")
        count = 1
        for i in hand:
            face = i.split()[2][0]
            if count != len(hand):
                print("|    " + face + "    |", end=" ")
                count += 1
            else:
                print("|    " + face + "    |")
        count = 1
        for i in hand:
            num = i.split()[0][0]
            if count != len(hand):
                if num == "1":
                    num = num + "0"
                    print("|       " + num + "|", end=" ")
                else:
                    print("|        " + num + "|", end=" ")
                count += 1
            else:
                if num == "1":
                    num = num + "0"
                    print("|       " + num + "|")
                else:
                    print("|        " + num + "|")
        count = 1
        for i in hand:
            if count != len(hand):
                print("-----------", end=" ")
                count += 1
            else:
                print("-----------")
