# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

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
