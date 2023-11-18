serving_cost = 1.00
labor_cost = 7.50
rental_cost = 800
utilities_cost = 150
advertising_cost = 100
selling_price = 4.0
servings_sold = 1000

# Used to control loop
run_flag = True

while run_flag == True:
    #First the menu appears.
    print("Expenses: ")
    print("1. Cost per serving:", serving_cost)
    print("2. Labor rate per hour:", labor_cost)
    print("3. Shop rental per month:", rental_cost)
    print("4. Utilities per month:", utilities_cost)
    print("5. Advertising budget per month:", advertising_cost)
    print("Income: ")
    print("6. Selling price (each):", selling_price)
    print("7. Servings sold per month:", servings_sold)
    print("Analysis: ")
    print("8. Profit/Loss Calculation ")
    print("9. \"What If\" analysis with 10% variance")
    # There is 1 employee working 8 hours per day, 6 days a week, every month
    labor_per_month = labor_cost * 8 * 6 * 4
    # Defining local variables to use in equations
    expense_list = [(serving_cost * servings_sold), labor_per_month, rental_cost, utilities_cost, advertising_cost]
    total_expense = (sum(expense_list))
    total_profit = float(selling_price * servings_sold)
    total_sum = round((total_profit - total_expense), 2)
    per_serving = (total_sum / servings_sold)
    # Get selection
    menuselection = input("Enter Selection (0 to Exit): ")
    if menuselection == "1":
        serving_cost = float(input("Enter cost per serving: "))
    elif menuselection == "2":
        labor_cost = float(input("Enter labor rate per hour: "))
    elif menuselection == "3":
        rental_cost = float(input("Enter shop rental cost per month: "))
    elif menuselection == "4":
        utilities_cost = float(input("Enter cost of utilities per month: "))
    elif menuselection == "5":
        advertising_cost = float(input("Enter advertising budget per month: "))
    elif menuselection == "6":
        selling_price = float(input("Enter selling price (each): "))
    elif menuselection == "7":
        servings_sold = int(input("Enter servings sold per month: "))
    elif menuselection == "8":
        print(total_sum)
        print(per_serving)
        print(f"The Ice Cream Shop will have a monthly profit/loss of {total_sum} or {per_serving} per serving.")
    #Find the profit/loss when varying the expenses and income by +/-10%.
    elif menuselection == "9":
        variation = range(-10, 11, 2)
        print("Varying the Expenses +/-10%:")
        for v in variation:
            vpercent = v * 0.01
            varied_total_expense = total_expense + (total_expense * vpercent)
            print("Percent: " + str(v) + " Expenses: " + str(round(float(varied_total_expense), 1)) + " Profit/Loss: " + str(round(float(total_profit - varied_total_expense), 1)))
        print("Varying the Income +/-10%:")
        for v in variation:
            vpercent = v * 0.01
            varied_total_profit = total_profit + (total_profit * vpercent)
            print("Percent: " + str(v) + " Income: " + str(varied_total_profit) + " Profit/Loss: " + str((varied_total_profit - total_expense)))
    elif menuselection == "0":
        break
    else:
        print("Invalid Input.")
        continue
