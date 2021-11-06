#load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.
# Your program should output something like:
# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

import json
from collections import Counter

dates = []

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)
for i in birthdays: #for x in birthdays.values():
    d = birthdays.get(i) #month.append(x.split()[1])
    dates.append((d.split(' '))[1])

count = Counter(dates)
dates_list = list(count.keys())

counter = 0
while counter < len(dates_list):
    print("{}: {}".format(dates_list[counter],count[dates_list[counter]]))
    counter += 1
