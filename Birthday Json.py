#Modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

#Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

birthdays = {"Will": "01/03/2021", "Bill": "02/03/2021"}
names = []

print("Welcome to the birthday dictionary. We know the birthdays of:")
for i in birthdays:
    print(i)

user_pick = input("Enter a name: ")


print(
    "{}'s birthday is {}.".format(
        user_pick.capitalize(), (birthdays.get(user_pick.capitalize(), "not found"))
    )
)