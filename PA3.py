# Budget Planner

'''
Make a code that help individuals who struggle to save money become more aware of how they are spending it and what they are spending it on. This Budget Planner will include: Categories, price, and certain messages that keep you in check (ex. "Maybe try to limit spendings on {category}").

'''

Expenses_file = "expenses.txt"

def add_expenses(expenses):
    print("\nAvailable categories:")
    for category in expenses:
        print(f"{category}")

#def view_summary(expenses, limits):

def save_expenses(filename, expenses):
    with open(filename, "w") as f:
        for category, items in expenses.items():
            for amount, note in items:
                f.write(f"{category},{amount},{note}\n")
    print("All expenses are saved!\n")

def main():
    name = input("Hello! Please enter your name > ")
    print(f"Hello {name}!")

    expenses = {
            "1. electronics": [],
            "2. clothing/shoes": [],
            "3. beverages": [],
            "4. food": [],
            "5. makeup": [],
            "6. fragrances": [],
            "7. household essentials (ex. furniture, garden necessities, groceries, decorations, car payments, fuel)": [],
            "8. sports/fitness": [],
            "9. health (ex. medicine)": [],
            "10. media (ex. game expenses)": [],
            "11. tobacco": [],
            "12. toys/hobbies": [],
            "13. luxury goods (ex. high end jewerly, expensive watches)": [],
            "14. pets/pet necessities (ex. cat food)": [],
            "15. taxes!": []
        }
        #limits
    limits = {
            "1. electronics": 500,
            "2. clothing/shoes": 100,
            "3. beverages": 50,
            "4. food": 200,
            "5. makeup": 30,
            "6. fragrances": 50,
            "7. household essentials (ex. furniture, garden necessities, groceries, decorations, car payments, fuel)": 700,
            "8. sports/fitness": 50,
            "9. health (ex. medicine)": 0,
            "10. media (ex. game expenses)": 25,
            "11. tobacco": 10,
            "12. toys/hobbies": 30,
            "13. luxury goods (ex. high end jewerly, expensive watches)": 100,
            "14. pet necessities (ex. cat food)": 150,
            "15. taxes!": 0
        }


    while True:
        print("\nWhat would you like to do > ")
        print("1. Add an expense")
        print("2. View Summary")
        print("3. Quit")

        choice = input("Choose a number > ")

        if choice == "1":
            add_expenses(expenses)

        elif choice == "2":
            view_summary(expenses, limits)

        elif choice == "3":
            save_expenses(Expenses_file, expenses)
            print("Your expenses have been saved. Goodbye!")
            break
        else:
            print("Sorry! Either type: 1, 2, 3\n")


#To run the code
if __name__ == "__main__":
    main()