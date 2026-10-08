
import csv
import re

# Read movie records from CSV
with open("movies.csv", "r", encoding="utf-8-sig", newline="") as file:
    movies = list(csv.DictReader(file))

# Display movie information
def display_movies(records):
    if not records:
        print("No movies found.")
        return

    for movie in records:
        print("ID:", movie["Movie ID"].strip())
        print("Title:", movie["Title"].strip() or "N/A")
        print("Genre:", movie["Genre"].strip() or "N/A")
        print("Year:", movie["Year"].strip() or "N/A")
        print("Rating:", movie["Rating"].strip() or "N/A")
        print("-" * 30)

# Menu-driven movie collection system
while True:
    print("\n1. Display All Movies")
    print("2. Search by Movie ID")
    print("3. Search by Title (Regex)")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        display_movies(movies)

    elif choice == "2":
        movie_id = input("Enter Movie ID: ").strip()
        matches = [m for m in movies if m["Movie ID"].strip().lower() == movie_id.lower()]
        display_movies(matches)

    elif choice == "3":
        pattern = input("Enter title or regex: ").strip()
        if not pattern:
            print("Please enter a search pattern.")
            continue
        try:
            matches = [m for m in movies if re.search(pattern, m["Title"].strip(), re.IGNORECASE)]
            display_movies(matches)
        except re.error:
            print("Invalid regular expression.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
