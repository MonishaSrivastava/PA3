#-------------------
#BUDGET PLANNER
#-------------------

import datetime

expenses_file = "expenses.txt"

def add_expenses(expenses):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nAvailable categories:")
    for category in expenses:
        print(f"{category}") #Prints out all categories

    category_name = ""

    while True:
        choice = input("Which category do you want to add expenses to? (Type the number) > ")

        for category in expenses:
            if category.startswith(choice + "."):
                category_name = category
                break

        if category_name != "":
            print(f"\nYou selected: {category_name}")
            break #exit once valid
        else:
            print("\nInvalid category number!")
            break
    
    if category_name == "":
        print("No valid category selected.")
        return

    try:
        amount = float(input("Enter the amount you spent: $"))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return

    note = input("Add a short note (recommended) > ")

    expenses[category_name].append((amount, note, date))
    print(f"\nAdded ${amount:.2f} to {category_name}!")

def save_expenses(filename, expenses):
    with open(filename, "w") as f: #opens file in write mode and overwrites the file with users budget/expenses
        for category, items in expenses.items():
            for amount, note, date in items:
                f.write(f"{category},{amount},{note},{date}\n") #overwrites each category, amount, and note in the expenses.txt file
    print("All expenses are saved!\n")

def view_summary(expenses, limits):
    print("Expense summary!!!")
    print("-" * 60)

    total_expenses = 0
    user_has_expenses = False

    for category, items in expenses.items():
        if items:  # show only if user actually spent here
            user_has_expenses = True
            total = sum(amount for amount, note, date in items)
            total_expenses += total
            limit = limits.get(category, 0)

            for amount, note, date in items:
                print(f"${amount:.2f} on {date} ({note}) spent (Limit: ${limit:.2f})")  

            if total > limit: #if the total is higher than the limit, it will make a little caution note saying "Over Budget!"
                print("Over budget!")

            elif total < limit:
                print(f"${limit - total:.2f} remaining.")

    if not user_has_expenses:
        print("No expenses recorded yet.")

    else:
            print("-" * 60)
            print(f"Total spent across all categories: ${total_expenses:.2f}")

    print("-" * 60)

def add_limits(limits):
    print("\nLimits set:")
    for category, limit in limits.items(): 
        print(f"{category} : ${limit}")

    while True:
        choice = input("\nEnter the category number to change > ")

        category_name = ""
        for category in limits:
            if category.startswith(choice + "."):
                category_name = category
                break

        if category_name != "":
            print(f"\nYou selected: {category_name}")
            break
        else:
            print("Invalid category number!")

    try:
        new_limit = float(input(f"Enter new limit for {category_name}: $")) #float basically adds decimals points ex. instead of 10 it would return as 10.0

    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return

    limits[category_name] = new_limit
    print(f"\nUpdated limit for {category_name} to ${new_limit:.2f}")

def load_expenses(filename, expenses):
    try:
        with open(filename, "r") as f: #opens file in read mode
            for line in f:
                # Remove any extra spaces or newlines from the line
                clean_line = line.strip()

                # Split the line by commas into separate parts
                parts = clean_line.split(",")

                # Each line should have 4 parts: category, amount, note, and date
                if len(parts) != 4:
                    continue  # move to next line if data is missing or broken

                category = parts[0]
                amount_text = parts[1]
                note = parts[2]
                date = parts[3]
                try:
                    amount = float(amount_text)
                except ValueError:
                    continue  # skip bad data
                if category in expenses:
                    expenses[category].append((amount, note, date))
        print("\nPrevious expenses loaded successfully!\n")
    except FileNotFoundError:
        print("\nNo previous expense file found. Starting fresh!\n")


def main():
    name = input("Hello! Please enter your name > ")
    print(f"\nHello {name}!")

    expenses = {
            "1. electronics": [],
            "2. clothing/shoes": [],
            "3. beverages": [],
            "4. food (ex. takeout, groceries)": [],
            "5. makeup": [],
            "6. fragrances": [],
            "7. household lifestyle/essentials (ex. furniture, garden necessities, decorations)": [],
            "8. sports/fitness": [],
            "9. health (ex. medicine)": [],
            "10. media (ex. game expenses)": [],
            "11. tobacco": [],
            "12. toys/hobbies": [],
            "13. pet necessities (ex. cat food)": [],
            "14. taxes/loans": []
        }
        #limits
    limits = {
            "1. electronics": 50,
            "2. clothing/shoes": 20,
            "3. beverages": 20,
            "4. food (ex. takeout, groceries)": 15,
            "5. makeup": 10,
            "6. fragrances": 30,
            "7. household lifestyle/essentials (ex. furniture, garden necessities, decorations)": 40,
            "8. sports/fitness": 25,
            "9. health (ex. medicine)": 0,
            "10. media (ex. game expenses)": 10,
            "11. tobacco": 10,
            "12. toys/hobbies": 30,
            "13. pet necessities (ex. cat food)": 20,
            "14. taxes/loans": 0
        }

    load_expenses(expenses_file, expenses)
    while True:
        print("\nWhat would you like to do > ")
        print("1. Add an expense")
        print("2. View Summary")
        print("3. Change limits (There is already a base limit set for you, you may change it to your liking)")
        print("4. Quit")

        choice = input("Choose a number > ")

        if choice == "1":
            add_expenses(expenses)

        elif choice == "2":
            view_summary(expenses, limits)

        elif choice == "3":
            add_limits(limits)

        elif choice == "4":
            save_expenses(expenses_file, expenses)
            print("Your expenses have been saved. Goodbye!")
            break
        else:
            print("Sorry! Either type: 1, 2, 3, 4\n")
            continue


#To run the code
if __name__ == "__main__":
    main()