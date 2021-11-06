# Modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

# Birthday search
import json

print("Welcome to the birthday dictionary. We know the birthdays of:")
with open("birthdays.json", "r") as f:
    scientists = json.load(f)
for i in scientists:
    print(i)

user_pick = input("Enter a name: ")
new_scientist = input("Now enter a new scientist's name: ")
birth_date = input("Now enter their birth date: ")
scientists[new_scientist] = birth_date

with open("birthdays.json", "w") as w:
    json.dump(scientists, w)

print("{}'s birthday is {}.".format(user_pick.title(), (scientists.get(user_pick.title(), "not found"))))
