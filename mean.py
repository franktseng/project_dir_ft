import sys

sum = 0
counter =0

# sum all numbers in the standard input
for n in sys.stdin:

	sum+=float(n)
	counter+=1


print sum/counter
