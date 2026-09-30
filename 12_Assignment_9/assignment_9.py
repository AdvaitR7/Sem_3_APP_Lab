import csv
import json
with open("student_info.csv","r") as csv_file :
  csv_reader = csv.DictReader(csv_file)
  data = list(csv_reader)
with open("students.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
print("CSV data successfully converted to JSON!")
print("Output file: students.json")