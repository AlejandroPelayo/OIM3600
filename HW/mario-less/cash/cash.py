def get_cents() -> int:
    """
    Ask how many cents the customer is owed, and return the number
    """
    while True:
        try:
            cents = int(input("How many cents are owed? "))
            if 0 <= cents <= 99:
                return cents
            else:
                print("please input a number between 0-99")
        except ValueError:
            print("Input a valid number")


def calculate_quarters(cents: int) -> int:
    """
    Calculate the number of quarters to give the customer
    """
    quarters = cents // 25
    return quarters


def calculate_dimes(cents: int) -> int:
    """
    Calculate the number of dimes to give the customer
    """
    dimes = cents // 10
    return dimes 


def calculate_nickels(cents: int) -> int:
    """
    Calculate the number of nickels to give the customer
    """
    nickels = cents // 5
    return nickels


def calculate_pennies(cents: int) -> int:
    """
    Calculate the number of pennies to give the customer
    """
    pennies = cents
    return pennies

def main():
    """
#     You don't need to change any code in this function
#     """
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print the total number of coins to give the customer
    print(f"The total number of coins is {coins}.")
    print(f"quarters {quarters}, dimes {dimes}, nickels {nickels}, pennies {pennies}")


if __name__ == '__main__':
    main()