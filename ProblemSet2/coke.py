def main():
    coke = 50
    coins = 0

    while coins < coke:
        print(f"Amount Due: {coke - coins}")
        coin_input = int(input("Insert Coin: "))
        if coin_input in [5, 10, 25]:
            coins += coin_input

    change = coins - coke
    print(f"Change Owed: {change}")
main()


'''
implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


A more fun way to code but does not pass the CS50 tests
def main():
    coke = 50
    coins = 0

    while coins < coke:
        coin = int(input("Insert coins (Only accepts 5, 10, 25 denominations): "))
        if coin in [5, 10, 25]:
            coins += coin
            if coins < coke:
                print(f"Amount Due: {coke - coins} cents")
            if coins >= coke:
                print("Enjoy your coke!")
        else:
            print("Invalid coin. Please insert a valid coin.")

    change = coins - coke
    print(f"Change Owed: {change} cents")

main()
'''
