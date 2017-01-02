### Bubble sort implementation in Python 2.7 ###

# Getting input to create an unsorted list
print("Please enter numbers to generate a list; type 'END' when done.")
list = []
while True:
	input = raw_input("Input: ")
	if input == 'END':
		break
	try:
		list.append(float(input))
	except ValueError:
		print "Invalid input! Enter a number or type 'END'..."
	
# Bubble sort algorithm
def bblsort(numList):
	for i in range(len(numList)-1):
		for j in range(len(numList)-1-i):
			if numList[j] > numList[j+1]:
				temp = numList[j+1]
				numList[j+1] = numList[j]
				numList[j] = temp
	return(numList)
	
# Call bubble sort function on input list
print "Sorted list: " + str(bblsort(list))
