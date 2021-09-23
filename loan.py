# Demos lists and loops, range in an example repayment calculator

money_owed = float(input("How much money do you owe?\n"))
apr = float(input("What is the APR?\n"))
payment = float(input("What will your monthly payment be?\n"))
months = int(input("How many months do you want to see results for?\n"))

# divide APR by 100 to get a percentage and by 12 to make it monthly
monthly_rate = apr / 100 / 12

for i in range(months):
    # Add interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if money_owed - payment < 0:
        print("The last payment is", money_owed)
        print("You paid off the loan in", i + 1, "months")
        break

    # make payment
    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now I owe", money_owed)
