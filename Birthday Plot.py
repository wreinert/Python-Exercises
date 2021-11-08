#In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.

import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

dates = []

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)
for i in birthdays: #for x in birthdays.values():
    d = birthdays.get(i) #month.append(x.split()[1])
    dates.append((d.split(' '))[0])

count = Counter(dates)
dates_list = list(count.keys())

counter = 0
while counter < len(dates_list):
    print("{}: {}".format(dates_list[counter],count[dates_list[counter]]))
    counter += 1

#Chart
output_file("plot.html")

x = list(set(count.keys())) #months
y = [] #count
x_categories = x #category names

for b in x: #adds the number of birthdays to y axis
    y.append(count[b])

#drawing the chart
plot = figure(x_range=x_categories)
plot.vbar(x=sorted(x), top=y, width=0.5)
show(plot)




