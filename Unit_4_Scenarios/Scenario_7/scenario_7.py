
import numpy as np
import pandas as pd

# Create a NumPy array of treatment costs
costs = np.array([12000, 25000, 18000, 45000, 8000, 32000, 20000, 27000])

# Create a patient treatment DataFrame
patients = pd.DataFrame({
    "Patient ID": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008"],
    "Name": ["Aarav", "Priya", "Rohan", "Neha", "Vikram", "Meera", "Arjun", "Sneha"],
    "Treatment Cost": costs
})

# Menu-driven treatment cost analysis
while True:
    print("\n1. Display All Patients")
    print("2. Show Treatment Cost Statistics")
    print("3. Show Patients with Cost Above Rs. 20,000")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        print("\nPatient Treatment Records:")
        print(patients.to_string(index=False))

    elif choice == "2":
        print("\nMean Treatment Cost:", np.mean(costs))
        print("Maximum Treatment Cost:", np.max(costs))
        print("Minimum Treatment Cost:", np.min(costs))

    elif choice == "3":
        print("\nPatients with Treatment Cost Above Rs. 20,000:")
        print(patients[patients["Treatment Cost"] > 20000].to_string(index=False))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
