#-------------------
#BUDGET PLANNER
#-------------------

import datetime #allows python to import the current date/time https://www.w3schools.com/python/python_datetime.asp

expenses_file = "expenses.txt" #name of the file where everything will be saved

def add_expenses(expenses):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #datetime.now returns the name of the weekday  and datetime.strftime is used for formatting, it takes 1 parameter to specify the format of the returned string. (ex. %Y = year)
    print("\nAvailable categories:")
    for category in expenses: #goes through every key (category) in expenses
        print(f"{category}") #Prints out all categories

    category_name = "" #stores the chosen category name later 

    while True:
        choice = input("Which category do you want to add expenses to? (Type the number) > ")

        for category in expenses: #goes through each category to find one matching the number entered.
            if category.startswith(choice + "."): #if statement: verifies input matches a valid category number. Startwith() function method return true if string (category) starts with the specified value (1)--python uses this to verify if the category starts with 1, 2, 3, etc
                category_name = category
                break #exits the loop once verified true

        if category_name != "": #true if a valid category was found
            print(f"\nYou selected: {category_name}")
            break #exit while loop once valid
        else:
            print("\nInvalid category number!")
            break
    
    if category_name == "": #stops function if nothing typed or if no valid category was chosen
        print("No valid category selected.")
        return

    try: #attempts to convert user input into a float
        amount = float(input("Enter the amount you spent: $")) #float is used to return decimal points ex. if you type 138.89 it won't show up as error as it would if you removed the float https://www.w3schools.com/python/ref_func_float.asp
    except ValueError: #runs if user enters a non-numeric number
        print("\nInvalid input. Please enter a number.")
        return

    note = input("Add a short note (recommended) > ")

    expenses[category_name].append((amount, note, date)) #adds tuple to selected category (yay i learnt tuples last proj)
    print(f"\nAdded ${amount:.2f} to {category_name}!")

def save_expenses(filename, expenses):
    with open(filename, "w") as f: #opens file in write mode and overwrites the file with users budget/expenses
        for category, items in expenses.items(): #goes through each category and its list of expenses
            for amount, note, date in items: #nested for loop (for loop inside for loop) this writes each expense tuple
                f.write(f"{category},{amount},{note},{date}\n") #overwrites each category, amount, and note in the expenses.txt file
    print("All expenses are saved!\n")

def view_summary(expenses, limits):
    print("Expense summary!!!")
    print("-" * 60)

    total_expenses = 0
    user_has_expenses = False #if user doesn't have spending it will be false

    for category, items in expenses.items(): #checks each spending category
        if items:  # show only if user actually spent here
            user_has_expenses = True
            total = sum(amount for amount, note, date in items) #generator inside sum() totals all expenses
            total_expenses += total
            limit = limits.get(category, 0) #retrieves category limit (default = 0). .get() returns the value (0) of the item with a specified key(category) https://www.w3schools.com/python/ref_dictionary_get.asp -- without this it would show an error for all limits set to 0 such as category health

            for amount, note, date in items: #displays each individual expense record
                print(f"${amount:.2f} on {date} ({note}) spent (Limit: ${limit:.2f})")  

            if total > limit: #if the total is higher than the limit, it will make a little caution note saying "Over Budget!"
                print("Over budget!")

            elif total < limit: #shows how much money remains under the limit
                print(f"${limit - total:.2f} remaining.")

    if not user_has_expenses: #without this it won't run if the user didn't have expenses 
        print("No expenses recorded yet.") #will show this if user does not have any expenses yet

    else: #runs when user has expenses
            print("-" * 60)
            print(f"Total spent across all categories: ${total_expenses:.2f}")

    print("-" * 60)

def add_limits(limits):
    print("\nLimits set:")
    for category, limit in limits.items(): #prints all category-limit pairs
        print(f"{category} : ${limit}")

    while True: #continues until a valid category is selected
        choice = input("\nEnter the category number to change > ")

        category_name = ""
        for category in limits: #searches for a category starting with the entered number
            if category.startswith(choice + "."): #verifies if input matches an existing category
                category_name = category
                break

        if category_name != "": #if its a valid input path it will display your category name and move on to the next question
            print(f"\nYou selected: {category_name}")
            break
        else:
            print("Invalid category number!")

    try: #attempts to convert user number into float
        new_limit = float(input(f"Enter new limit for {category_name}: $")) #float basically adds decimals points ex. instead of 10 it would return as 10.0

    except ValueError: #handles invalid number input
        print("\nInvalid input. Please enter a number.")
        return

    limits[category_name] = new_limit #updates chosen limit
    print(f"\nUpdated limit for {category_name} to ${new_limit:.2f}")

def load_expenses(filename, expenses):
    try: #attempt to open and read the saved file
        with open(filename, "r") as f: #opens file in read mode
            for line in f: #reads the file line for line
                # Remove any extra spaces or newlines from the line
                clean_line = line.strip()

                # Split the line by commas into separate parts
                parts = clean_line.split(",")

                # Each line should have 4 parts: category, amount, note, and date. len function returns the number of characters in the string
                if len(parts) != 4: #skips incomplete lines https://www.w3schools.com/python/ref_func_len.asp
                    continue  # move to next line if data is missing or broken

                category = parts[0]
                amount_text = parts[1]
                note = parts[2]
                date = parts[3]
                try: #attempts to convert amount into a float -- 10 to 10.00
                    amount = float(amount_text)
                except ValueError:
                    continue  # skip bad data/entries with invalid input
                if category in expenses: #adds the expense if category is valid
                    expenses[category].append((amount, note, date)) #tuple
        print("\nPrevious expenses loaded successfully!\n")
    except FileNotFoundError:
        print("\nNo previous expense file found. Starting fresh!\n")


def main():
    name = input("Hello! Please enter your name > ")
    print(f"\nHello {name}!")

#dictionary for categories and expense bracket

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
        #limit dictionary
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

    load_expenses(expenses_file, expenses) # load previous data before showing menu


    while True: #keeps running until user types 4 (quit)
        print("\nWhat would you like to do > ")
        print("1. Add an expense")
        print("2. View Summary")
        print("3. Change limits (There is already a base limit set for you, you may change it to your liking)")
        print("4. Quit")

        choice = input("Choose a number > ")

        if choice == "1": #user selects to add expense
            add_expenses(expenses)

        elif choice == "2": #user selects to view the summary of their expenses and if they are over the budget
            view_summary(expenses, limits)

        elif choice == "3": #user selects to add limits
            add_limits(limits)

        elif choice == "4": #user selects to save expenses and quits
            save_expenses(expenses_file, expenses)
            print("Your expenses have been saved. Goodbye!")
            break
        else: #invalid user input
            print("Sorry! Either type: 1, 2, 3, 4\n")
            continue #restarts the while loop and prints out the options initally given


#To run the code
if __name__ == "__main__":
    main()