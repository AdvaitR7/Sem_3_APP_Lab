class Patient:
    def __init__(self, patient_id, name, treatment_cost, category):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = category

    def display(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Treatment Cost: {self.treatment_cost}")
        print(f"Category: {self.category}")
        print("-" * 30)


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_all_records(self):
        if not self.patients:
            print("No patient records found.")
        else:
            for patient in self.patients:
                patient.display()


hospital = Hospital()

n = int(input("Enter number of patients: "))

for i in range(n):
    print(f"\nEnter details of patient {i + 1}")
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    treatment_cost = float(input("Enter Treatment Cost: "))
    category = input("Enter Category (General/Special): ")
    patient = Patient(patient_id, name, treatment_cost, category)
    hospital.add_patient(patient)

print("\nAll Patient Records:")
hospital.display_all_records()