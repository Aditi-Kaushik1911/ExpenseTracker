import csv
import datetime
import pandas as pd

CSV_FILE = "expenses.csv"

# Create CSV file with headers if not exists
def initialize_csv():
    try:
        with open(CSV_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass


# Add a new expense
def add_expense():
    date = datetime.date.today()
    category = input("Enter category (Food, Travel, Shopping, Bills, Other): ")
    amount = float(input("Enter amount: "))
    description = input("Enter short description: ")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("\n✔ Expense added successfully!\n")


# View all expenses
def view_expenses():
    try:
        df = pd.read_csv(CSV_FILE)
        print("\n===== ALL EXPENSES =====\n")
        print(df.to_string(index=False))
    except FileNotFoundError:
        print("No expenses recorded yet.")


# Monthly summary
def monthly_summary():
    df = pd.read_csv(CSV_FILE)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    print("\n===== MONTHLY SUMMARY =====\n")
    summary = df.groupby('Month')['Amount'].sum()
    print(summary)


# Category-wise spending
def category_summary():
    df = pd.read_csv(CSV_FILE)
    print("\n===== CATEGORY SUMMARY =====\n")
    summary = df.groupby('Category')['Amount'].sum()
    print(summary)


# Main Menu
def main_menu():
    initialize_csv()

    while True:
        print("\n===== EXPENSE TRACKER MENU =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Spending Summary")
        print("4. Category-wise Spending Summary")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("\nThank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()
