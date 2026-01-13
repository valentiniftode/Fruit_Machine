import random
import time


def get_cashout(row1, row2, row3, bet):
    if row1[0] == row1[1] == row1[2] == row1[3] == row1[4] == row2[0] == row2[1] == row2[2] == row2[3] == row2[4] == row3[0] == row3[1] == row3[2] == row3[3] == row3[4]:
        if row1[0] == "🍒":
            return bet * 50000
        elif row1[0] == "🍋":
            return bet * 50000
        elif row1[0] == "🍎":
            return bet * 50000
        elif row1[0] == "🍓":
            return bet * 100000
        elif row1[0] == "🍐":
            return bet * 100000
        elif row1[0] == "🍊":
            return bet * 250000
        elif row1[0] == "🍍":
            return bet * 250000
        elif row1[0] == "🥥":
            return bet * 500000
        elif row1[0] == "🍉":
            return bet * 750000
        elif row1[0] == "🥝":
            return bet * 750000
        elif row1[0] == "🍌":
            return bet * 2500000
        elif row1[0] == "🍑":
            return bet * 10000000
        else:
            return 0

    elif row1[0] == row1[1] == row1[2] == row1[3] == row1[4] == row2[0] == row2[1] == row2[2] == row2[3] == row2[4] or row2[0] == row2[1] == row2[2] == row2[3] == row2[4] == row3[0] == row3[1] == row3[2] == row3[3] == row3[4]:
        if row1[0] or row3[0] == "🍒":
            return bet * 1000
        elif row1[0] or row3[0] == "🍋":
            return bet * 1000
        elif row1[0] or row3[0] == "🍎":
            return bet * 1000
        elif row1[0] or row3[0] == "🍓":
            return bet * 2500
        elif row1[0] or row3[0] == "🍐":
            return bet * 2500
        elif row1[0] or row3[0] == "🍊":
            return bet * 5000
        elif row1[0] or row3[0] == "🍍":
            return bet * 5000
        elif row1[0] or row3[0] == "🥥":
            return bet * 5000
        elif row1[0] or row3[0] == "🍉":
            return bet * 7500
        elif row1[0] or row3[0] == "🥝":
            return bet * 7500
        elif row1[0] or row3[0] == "🍌":
            return bet * 15000
        elif row1[0] or row3[0] == "🍑":
            return bet * 25000
        else:
            return 0

    elif row1[0] == row1[1] == row1[2] == row1[3] == row1[4] or row2[0] == row2[1] == row2[2] == row2[3] == row2[4] or row3[0] == row3[1] == row3[2] == row3[3] == row3[4]:
        if row1[0] or row2[0] or row3[0] == "🍒":
            return bet * 100
        elif row1[0] or row2[0] or row3[0] == "🍋":
            return bet * 100
        elif row1[0] or row2[0] or row3[0] == "🍎":
            return bet * 100
        elif row1[0] or row2[0] or row3[0] == "🍓":
            return bet * 150
        elif row1[0] or row2[0] or row3[0] == "🍐":
            return bet * 150
        elif row1[0] or row2[0] or row3[0] == "🍊":
            return bet * 250
        elif row1[0] or row2[0] or row3[0] == "🍍":
            return bet * 250
        elif row1[0] or row2[0] or row3[0] == "🥥":
            return bet * 250
        elif row1[0] or row2[0] or row3[0] == "🍉":
            return bet * 350
        elif row1[0] or row2[0] or row3[0] == "🥝":
            return bet * 350
        elif row1[0] or row2[0] or row3[0] == "🍌":
            return bet * 500
        elif row1[0] or row2[0] or row3[0] == "🍑":
            return bet * 1000
        else:
            return 0

    elif row1[0] == row1[1] == row1[2] == row1[3] or row1[1] == row1[2] == row1[3] == row1[4]:
        if row1[0] or row1[4] == "🍒":
            return bet * 10
        elif row1[0] or row1[4] == "🍋":
            return bet * 10
        elif row1[0] or row1[4] == "🍎":
            return bet * 10
        elif row1[0] or row1[4] == "🍓":
            return bet * 15
        elif row1[0] or row1[4] == "🍐":
            return bet * 15
        elif row1[0] or row1[4] == "🍊":
            return bet * 25
        elif row1[0] or row1[4] == "🍍":
            return bet * 25
        elif row1[0] or row1[4] == "🥥":
            return bet * 25
        elif row1[0] or row1[4] == "🍉":
            return bet * 35
        elif row1[0] or row1[4] == "🥝":
            return bet * 35
        elif row1[0] or row1[4] == "🍌":
            return bet * 50
        elif row1[0] or row1[4] == "🍑":
            return bet * 100
        else:
            return 0

    elif row2[0] == row2[1] == row2[2] == row2[3] or row2[1] == row2[2] == row2[3] == row2[4]:
        if row2[0] or row2[4] == "🍒":
            return bet * 10
        elif row2[0] or row2[4] == "🍋":
            return bet * 10
        elif row2[0] or row2[4] == "🍎":
            return bet * 10
        elif row2[0] or row2[4] == "🍓":
            return bet * 15
        elif row2[0] or row2[4] == "🍐":
            return bet * 15
        elif row2[0] or row2[4] == "🍊":
            return bet * 25
        elif row2[0] or row2[4] == "🍍":
            return bet * 25
        elif row2[0] or row2[4] == "🥥":
            return bet * 25
        elif row2[0] or row2[4] == "🍉":
            return bet * 35
        elif row2[0] or row2[4] == "🥝":
            return bet * 35
        elif row2[0] or row2[4] == "🍌":
            return bet * 50
        elif row2[0] or row2[4] == "🍑":
            return bet * 100
        else:
            return 0

    elif row3[0] == row3[1] == row3[2] == row3[3] or row3[1] == row3[2] == row3[3] == row3[4]:
        if row3[0] or row3[4] == "🍒":
            return bet * 10
        elif row3[0] or row3[4] == "🍋":
            return bet * 10
        elif row3[0] or row3[4] == "🍎":
            return bet * 10
        elif row3[0] or row3[4] == "🍓":
            return bet * 15
        elif row3[0] or row3[4] == "🍐":
            return bet * 15
        elif row3[0] or row3[4] == "🍊":
            return bet * 25
        elif row3[0] or row3[4] == "🍍":
            return bet * 25
        elif row3[0] or row3[4] == "🥥":
            return bet * 25
        elif row3[0] or row3[4] == "🍉":
            return bet * 35
        elif row3[0] or row3[4] == "🥝":
            return bet * 35
        elif row3[0] or row3[4] == "🍌":
            return bet * 50
        elif row3[0] or row3[4] == "🍑":
            return bet * 100
        else:
            return 0

    elif row1[0] == row1[1] == row1[2] or row1[1] == row1[2] == row1[3] or row1[2] == row1[3] == row1[4]:
        if row1[0] or row1[3] or row1[4] == "🍒":
            return bet * 3
        elif row1[0] or row1[3] or row1[4] == "🍋":
            return bet * 3
        elif row1[0] or row1[3] or row1[4] == "🍎":
            return bet * 3
        elif row1[0] or row1[3] or row1[4] == "🍓":
            return bet * 5
        elif row1[0] or row1[3] or row1[4] == "🍐":
            return bet * 5
        elif row1[0] or row1[3] or row1[4] == "🍊":
            return bet * 7
        elif row1[0] or row1[3] or row1[4] == "🍍":
            return bet * 7
        elif row1[0] or row1[3] or row1[4] == "🥥":
            return bet * 7
        elif row1[0] or row1[3] or row1[4] == "🍉":
            return bet * 10
        elif row1[0] or row1[3] or row1[4] == "🥝":
            return bet * 10
        elif row1[0] or row1[3] or row1[4] == "🍌":
            return bet * 15
        elif row1[0] or row1[3] or row1[4] == "🍑":
            return bet * 20
        else:
            return 0

    elif row2[0] == row2[1] == row2[2] or row2[1] == row2[2] == row2[3] or row2[2] == row2[3] == row2[4]:
        if row2[0] or row2[3] or row2[4] == "🍒":
            return bet * 3
        elif row2[0] or row2[3] or row2[4] == "🍋":
            return bet * 3
        elif row2[0] or row2[3] or row2[4] == "🍎":
            return bet * 3
        elif row2[0] or row2[3] or row2[4] == "🍓":
            return bet * 5
        elif row2[0] or row2[3] or row2[4] == "🍐":
            return bet * 5
        elif row2[0] or row2[3] or row2[4] == "🍊":
            return bet * 7
        elif row2[0] or row2[3] or row2[4] == "🍍":
            return bet * 7
        elif row2[0] or row2[3] or row2[4] == "🥥":
            return bet * 7
        elif row2[0] or row2[3] or row2[4] == "🍉":
            return bet * 10
        elif row2[0] or row2[3] or row2[4] == "🥝":
            return bet * 10
        elif row2[0] or row2[3] or row2[4] == "🍌":
            return bet * 15
        elif row2[0] or row2[3] or row2[4] == "🍑":
            return bet * 20
        else:
            return 0

    elif row3[0] == row3[1] == row3[2] or row3[1] == row3[2] == row3[3] or row3[2] == row3[3] == row3[4]:
        if row3[0] or row3[3] or row3[4] == "🍒":
            return bet * 3
        elif row3[0] or row3[3] or row3[4] == "🍋":
            return bet * 3
        elif row3[0] or row3[3] or row3[4] == "🍎":
            return bet * 3
        elif row3[0] or row3[3] or row3[4] == "🍓":
            return bet * 5
        elif row3[0] or row3[3] or row3[4] == "🍐":
            return bet * 5
        elif row3[0] or row3[3] or row3[4] == "🍊":
            return bet * 7
        elif row3[0] or row3[3] or row3[4] == "🍍":
            return bet * 7
        elif row3[0] or row3[3] or row3[4] == "🥥":
            return bet * 7
        elif row3[0] or row3[3] or row3[4] == "🍉":
            return bet * 10
        elif row3[0] or row3[3] or row3[4] == "🥝":
            return bet * 10
        elif row3[0] or row3[3] or row3[4] == "🍌":
            return bet * 15
        elif row3[0] or row3[3] or row3[4] == "🍑":
            return bet * 20
        else:
            return 0

    elif row1[0] == row2[0] == row3[0] or row1[1] == row2[1] == row3[1] or row1[2] == row2[2] == row3[2] or row1[3] == row2[3] == row3[3] or row1[4] == row2[4] == row3[4]:
        if row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍒":
            return bet * 3
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍋":
            return bet * 3
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍎":
            return bet * 3
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍓":
            return bet * 5
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍐":
            return bet * 5
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍊":
            return bet * 7
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍍":
            return bet * 7
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🥥":
            return bet * 7
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍉":
            return bet * 10
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🥝":
            return bet * 10
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍌":
            return bet * 15
        elif row1[0] or row1[1] or row1[2] or row1[3] or row1[4] == "🍑":
            return bet * 20
        else:
            return 0

    else:
        return 0

def main():
    print("**************************************")
    print("***Welcome to Python Fruit Machine!***")
    print("******🍒🍋🍎🍓🍌🍑🍐🍊🍍🥥🍉🥝*****")
    print()
    time.sleep(1)
    print("******** Balance = $0 *********")
    balance = int(input("Please deposit funds: $"))
    time.sleep(1)
    print(f"Thank you! Your balance is ${balance}.")
    time.sleep(1)
    print("🍀🍀🍀🍀🍀🍀Good Luck!🍀🍀🍀🍀🍀🍀")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet: $")

        if not bet.isdigit():
            print("Please enter a valid bet!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Bet can't be zero!")
            continue

        balance -= bet

        time.sleep(1)
        print("Spinning...")
        time.sleep(1)

        symbols = "🍒", "🍋", "🍎", "🍓", "🍌", "🍑", "🍐", "🍊", "🍍", "🥥", "🍉", "🥝"
        chances = random.choices(symbols, weights=(100, 90, 80, 70, 5, 3, 60, 50, 40, 30, 20, 10), k=12)
        row1 = [random.choice(chances) for _ in range(5)]
        row2 = [random.choice(chances) for _ in range(5)]
        row3 = [random.choice(chances) for _ in range(5)]
        print("************************")
        print(" | ".join(row1))
        print("************************")
        print(" | ".join(row2))
        print("************************")
        print(" | ".join(row3))
        print("************************")

        payout = get_cashout(row1, row2, row3, bet)

        if payout >0:
            print(f"You won ${payout}!!!")
        else:
            print("😒 No luck this time 😒")

        balance += payout

        play_again = input("Spin again? (Y/N): ").upper()

        if play_again == "Y":
            main()
        elif play_again == "N":
            time.sleep(1)
            print("**************")
            print(f"Game ended. Your cashout is ${balance}")
            print("**************")
            print("Thank you for playing, have a nice day!")
            print("**************")
            quit()

if __name__ == "__main__":
    main()