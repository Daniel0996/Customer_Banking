# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.

    while True:
        savings_balance = input("Enter the savings account beginning balance: ")
        if is_balance_valid(savings_balance):
            savings_balance = float(savings_balance)
            break
    
    while True:
        savings_interest = input("Enter the savings account interest rate (APR): ")
        if is_interest_valid(savings_interest):
            savings_interest = float(savings_interest)
            break

    while True:
        savings_maturity = input("Enter the number of months to calcuate interest for the savings account: ")
        if is_month_valid(savings_maturity):
            savings_maturity = int(savings_maturity)
            break

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("After ", format(savings_maturity), "month(s), your savings account has earned $",
          format(interest_earned, ',.2f'), "in interest.  Your updated balance is $",
          format(updated_savings_balance, ',.2f') , '.\n'
    )


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    while True:
        cd_balance = input("Enter the CD account beginning balance: ")
        if is_balance_valid(cd_balance):
            cd_balance = float(cd_balance)
            break
    
    while True:
        cd_interest = input("Enter the CD account interest rate (APR): ")
        if is_interest_valid(cd_interest):
            cd_interest = float(cd_interest)
            break

    while True:
        cd_maturity = input("Enter the number of months to calcuate interest for the CD account: ")
        if is_month_valid(cd_maturity):
            cd_maturity = int(cd_maturity)
            break

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("After ", format(cd_maturity), "month(s), your CD account has earned $",
          format(interest_earned, ',.2f'), "in interest.  Your updated balance is $",
          format(updated_cd_balance, ',.2f') , '.\n'
    )


def is_balance_valid(balance_input):
    """ This function validates the balance input
        The input must be able to convert to a float, and must be positive.
    """
    try:
        if (float(balance_input) > 0):
            return True
        else:
            print("Balance amount can not be negative.")
            return False
    except ValueError:
        print("You have entered an invalid balance amount.")
        return False


def is_interest_valid(interest_rate):
    """ This function validates the input interest rate
        The input must be able to convert to a float, and must be positive.
    """
    try:
        if (float(interest_rate) > 0):
            return True
        else:
            print("Interest rate can not be negative.")
            return False
    except ValueError:
        print("You have entered an invalid interest rate.")
        return False


def is_month_valid(month):
    """ This function validates the input months
        The input must be able to convert to an integer, and must be positive.
    """
    try:
        if (int(month) > 0):
            return True
        else:
            print("The months must be a positive number.")
            return False
    except ValueError:
        print("You have entered an invalid month.")
        return False
    

if __name__ == "__main__":
    # Call the main function.
    main()
