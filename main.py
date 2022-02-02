from budgetclass import Budget

'''
food = Budget("food")
food.deposit(200)

travel = Budget("travel")
travel.deposit(300)
travel.withdraw(80)
'''
run = True
main_menu = "Please select an option:\n" + \
            "1. Deposit\n" + \
            "2. Withdraw\n" + \
            "3. Transfer\n" + \
            "4. View budget summary\n" + \
            "5. Exit\n"

while run:
    main_selection = int(input(main_menu))

    if main_selection == 5:
        run = False

    elif main_selection == 1:
        print("Please select an existing item or add a new one:\n"+
                "0. Return to main menu")
        count = 1
        budget_items, budget_balance = Budget.summary()
        for item in budget_items:
            print(f"{count}. {item}")
            count += 1
        
        print(f"{count}. Add a new item")
        selection = int(input())

        if selection == 0:
            continue
        elif selection == count:
            new_item = input("Enter new item name: ")
            amount = float(input("Enter amount: "))
            new_budget_obj = Budget(new_item)
            new_budget_obj.deposit(amount)
        else:
            for i in range(count):
                if selection == i+1:
                    print(budget_items[i])
                    amount = float(input("Enter amount: "))
                    temp_budget_obj = Budget(budget_items[i])
                    temp_budget_obj.deposit(amount)

        



