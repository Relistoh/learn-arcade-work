import random

REGULAR_THINGS = ["Money", "Watch", "a Phone", "Headphones"]
VALUABLE_THINGS = ["Money", "Jewels", "a Gold ring"]


def main():
    print("Welcome Thief!")
    print("Your goal is to steal as much as you can.")
    print("You have only one night left to earn money and pay your bills.")
    print("Good luck!")

    houses_left = 5
    owners_concern = 0
    total_money = 0
    hours_left = 24
    w = 0
    done = False
    while not done:
        if owners_concern >= 100:
            print("You were caught by the owners!")
            done = True
        elif owners_concern >= 50 and w == 0:
            print("Owners are starting to suspect.")
            w = 1
        elif hours_left <= 0:
            print("Your time is over!")
            done = True
        elif houses_left <= 0:
            print("There are no houses left!")
            done = True
        elif houses_left == 1:
            print("It is the last house!")
        elif total_money >= 200:
            print()
            print("You win!")
            print()
            print("Money earned:", total_money)
            print("Houses left:", houses_left)
            print("Hours left:", hours_left)
            print()
            done = True

        print()
        print("A. Look around.")
        print("B. Search for something valuable.")
        print("C. Go to the next house.")
        print("S. Status check.")
        print("E. Exit")
        print()

        player_choice = input("Your choice: ").upper()
        if player_choice == "E":
            done = True
        elif player_choice == "C":
            houses_left -= 1
            owners_concern = 0
            hours_left -= 1
            w = 0
        elif player_choice == "S":
            print("Houses left in neighborhood:", houses_left)
            print("Owners concern (%):", owners_concern)
            print("Hours left:", hours_left)
            print("Total money:", total_money)
        elif player_choice == "A":
            player_found = REGULAR_THINGS[random.randint(0, len(REGULAR_THINGS) - 1)]
            player_earned = random.randint(5, 10)
            print("You have found " + player_found + " which is worth " + str(player_earned) + ".")
            total_money += player_earned
            owners_concern += random.randint(5, 15)
            hours_left -= 0.1 * random.randint(5, 15)
        elif player_choice == "B":
            player_found = VALUABLE_THINGS[random.randint(0, len(VALUABLE_THINGS) - 1)]
            player_earned = random.randint(10, 20)
            print("You have found " + player_found + " which is worth " + str(player_earned) + ".")
            total_money += player_earned
            owners_concern += random.randint(15, 30)
            hours_left -= 0.1 * random.randint(10, 20)
        else:
            print("Sorry, I don't understand your choice.")


if __name__ == "__main__":
    main()