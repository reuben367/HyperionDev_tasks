# code to calculate return on simple and compound investments and monthly repayments on a home loan

import math

# provide users with choice of investment or bond calculator

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

finance_choice = input("Enter either 'investment' or 'bond' from the above to proceed: ")
finance_choice = finance_choice.lower()
finance_choice = finance_choice.strip()

while True:
    # if user choses "investment" ask for parameters of investment
    if finance_choice == "investment":
        deposit = int(input("Enter amount to be invested in £: "))
        rate = float(input("Enter interest rate as a %: "))
        time = int(input("Enter investment time in years: "))
        interest = input("Enter interest type (simple or compound): ")
        
        while True:
            # if user enters simple, calculate simple investment using simple interest formula and print result
            if interest == "simple":
                total_return = deposit * (1 + (rate / 100) * time)
                print(f"Total return is £{int(total_return)}")
                break
            # if user enters compound, calculate compound interest using compound formula and print result
            if interest == "compound":
                total_return = int(deposit * math.pow((1 + rate/100), time))
                print(f"Total return is £{int(total_return)}")
                break
            # if neither simple or compound selected, prompt user to reenter and return to relevant if statement, line 24b for simple line 24 for compound
            interest = input("You need to enter interest type, try again (simple or compound): ")
        break
    # if user choses bond ask for parameters of parameters of loan
    if finance_choice == "bond":
        current_value = int(input("Enter current house value in £: "))
        rate2 = float(input("Enter interest rate as a %: "))
        time2 = int(input("Enter repayment period in months: "))
        # calculate monthly repayments and print
        monthly_repayment = ((rate2/1200) * current_value) / (1 - (1 + (rate2/1200))**-time2)
        print(f"Monthly repayments are £{int(monthly_repayment)}")
        break
    # if user enters neither bond or investment, prompt user to reenter and retun to relevant if statement, line 16 for investment or line 37 for bond
    finance_choice = input("Error, you must enter either 'investment' or 'bond' to proceed: ")
    finance_choice = finance_choice.lower()
    finance_choice = finance_choice.strip()