from budgetclass import Budget

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

    elif main_selection == 2:
        print("Please select an item:\n"+
                "0. Return to main menu")
        count = 1
        budget_items, budget_balance = Budget.summary()
        for item in budget_items:
            print(f"{count}. {item}")
            count += 1
        
        selection = int(input())

        if selection == 0:
            continue

        else:
            for i in range(count):
                if selection == i+1:
                    print(budget_items[i])
                    amount = float(input("Enter amount: "))
                    temp_budget_obj = Budget(budget_items[i])
                    temp_budget_obj.withdraw(amount)

    
    elif main_selection == 3:
        print("Please select source item:\n")
        count = 1
        budget_items, budget_balance = Budget.summary()
        for item in budget_items:
            print(f"{count}. {item}")
            count += 1

        source_selection = int(input())
        
        amount = float(input("Enter amount: "))

        print("Please select destination item:\n")
        count = 1
        budget_items, budget_balance = Budget.summary()
        for item in budget_items:
            print(f"{count}. {item}")
            count += 1

        destination_selection = int(input())

        destination = Budget(budget_items[destination_selection-1])
        source = Budget(budget_items[source_selection-1])
        destination.deposit(amount)
        source.withdraw(amount)

        print(f"£{amount} was trasferred from {source.name} to {destination.name}")

    elif main_selection == 4:
        budget_items, budget_balance = Budget.summary()
        for item, balance in budget_items, budget_balance:
            print(f"{item}: {balance}\n")



