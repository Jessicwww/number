#
import random
r = random.randint(1, 100)
while True:
	num = input ('please enter an number')
	num = int(num)
	if r == num:
		print ('you are right')
		break
	else:
		if r > num:
			print ('larger')
		if r < num:
			print ('smaller')

