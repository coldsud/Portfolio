def tidbit_credit_plan(purchase_price):
    # Credit plan details
    down_payment_rate = 10  # 10% down payment
    annual_interest_rate = 12  # 12% annual interest rate
    monthly_payment_rate = 5  # 5% of the listed purchase price

    # Calculate initial values
    balance = purchase_price * (1 - down_payment_rate / 100)
    monthly_payment = purchase_price * (monthly_payment_rate / 100)

    # Print header for table
    print("{:<5} {:<20} {:<20} {:<20} {:<15} {:<20}".format(
        "Month", "Starting Balance", "Interest to Pay", "Principal to Pay", "Payment", "Ending Balance"
    ))

    # Calculate and display details for each month
    month = 1
    while balance > 0:
        starting_balance = balance

        # Check if monthly payment is greater than the remaining balance
        if monthly_payment > balance:
            payment = balance
            interest = 0
        else:
            interest = balance * (annual_interest_rate / 100) / 12
            payment = monthly_payment

        # Calculate principal and payment details
        principal = payment - interest
        
        # Calculate the ending balance
        ending_balance = starting_balance - payment

        # Print the details for the month
        print("{:<5} {:<20.2f} {:<20.2f} {:<20.2f} {:<15.2f} {:<20.2f}".format(
            month, starting_balance, interest, principal, payment, ending_balance
        ))

        # Update balance and month
        balance = ending_balance
        month += 1

# Get the purchase price and run the credit plan
purchase_price = float(input("Enter the purchase price: "))
tidbit_credit_plan(purchase_price)