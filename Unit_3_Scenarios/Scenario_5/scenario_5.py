
import csv

# Read patient records from CSV
with open("patients.csv", "r", encoding="utf-8-sig", newline="") as file:
    patients = list(csv.DictReader(file))

# Display patient details
def display_patients(records):
    if not records:
        print("No patients found.")
        return

    for patient in records:
        print("Patient ID:", patient["Patient ID"].strip() or "N/A")
        print("Name:", patient["Name"].strip() or "N/A")
        print("Age:", patient["Age"].strip() or "N/A")
        print("Gender:", patient["Gender"].strip() or "N/A")
        print("Diagnosis:", patient["Diagnosis"].strip() or "N/A")
        print("Doctor:", patient["Doctor"].strip() or "N/A")
        print("Admission Date:", patient["Admission Date"].strip() or "N/A")
        print("-" * 30)

# Menu-driven patient record system
while True:
    print("\n1. Display All Patients")
    print("2. Search by Patient ID")
    print("3. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        display_patients(patients)

    elif choice == "2":
        patient_id = input("Enter Patient ID: ").strip()
        matches = [p for p in patients if p["Patient ID"].strip().lower() == patient_id.lower()]
        display_patients(matches)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
