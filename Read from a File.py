#Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen.
#I have a .txt file for you, if you want to use it!
#Extra: Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
#and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database,
#and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category.
#To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

#Grabbing the whole text as string
'''
with open('read_from_a_file.txt', 'r') as read_file:
    readfile = read_file.read()
print(readfile)
'''

#Taking line by line
#Solution using dictionaries
counter_dict = {} #creates a dictionary
with open('read_from_a_file.txt') as f:
	line = f.readline() #reads the first line of the txt
	while line: #checks if lines is True
		line = line[3:-26] #takes only characters between the 3rd and the 26th from left to right "abbey"
		if line in counter_dict: 
			counter_dict[line] += 1 #if line in the dictionary, adds 1
		else:
			counter_dict[line] = 1 #if line not in the dictionary make it 1
		line = f.readline() #runs the next line in txt

print(counter_dict)


