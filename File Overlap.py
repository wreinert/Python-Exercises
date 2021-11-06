#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000 (divided by 1 and itself only), and the other .txt file has a list of happy numbers up to 1000.
'''
happynums = []
primenums = []
overlap = []

with open('file_overlap_happynumbers.txt') as n:
    line = n.readline()
    while line:
        happynums.append(line.split('\n')[0])
        line = n.readline()

with open('file_overlap_primenumbers.txt') as p:
    linep = p.readline()
    while linep:
        primenums.append(linep.split('\n')[0])
        linep = p.readline()

for a in happynums:
    if a in primenums:
        overlap.append(a)

print(happynums)
print(primenums)
print(overlap)
'''

#Solution using functions:
def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints('file_overlap_primenumbers.txt')
happieslist = filetolistofints('file_overlap_happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)
