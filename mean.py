import sys

sum = 0
counter =0


for n in sys.stdin:

	sum+=float(n)
	counter+=1


print sum/counter
