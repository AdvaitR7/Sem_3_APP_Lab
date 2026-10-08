
import numpy as np
import pandas as pd

# Create a NumPy array of prices
prices = np.array([45, 60, 120, 35, 90, 150, 25, 80])

# Create a grocery inventory DataFrame
inventory = pd.DataFrame({
    "Item": ["Rice", "Milk", "Oil", "Bread", "Eggs", "Tea", "Salt", "Sugar"],
    "Price": prices,
    "Quantity": [20, 8, 5, 15, 6, 12, 4, 18]
})

# Menu-driven inventory analysis
while True:
    print("\n1. Display All Grocery Items")
    print("2. Show Price Statistics")
    print("3. Show Items with Quantity Less Than 10")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        print("\nGrocery Inventory:")
        print(inventory.to_string(index=False))

    elif choice == "2":
        print("\nMean Price:", np.mean(prices))
        print("Median Price:", np.median(prices))
        print("Maximum Price:", np.max(prices))
        print("Minimum Price:", np.min(prices))

    elif choice == "3":
        print("\nItems with Quantity Less Than 10:")
        print(inventory[inventory["Quantity"] < 10].to_string(index=False))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
