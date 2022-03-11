
curNum = 1
prevNum = 0

total = 0

while curNum < 4000000:
	if curNum % 2== 0:
		total += curNum
	nextNum = prevNum + curNum
	prevNum = curNum
	curNum = nextNum
	print(prevNum) #prints each step in the fibbinaci sequence

print(total) #prints the sum of the even numbers
