#!/usr/bin/python3
import random
import time , os

matrix_char = "ABCDEFGHIJKLMNOPRSTWXQ@#                       "
line = []
tsize = os.get_terminal_size()
mwidth = tsize.columns
index = 0
print('\033[92m') # green color console

for i in range(mwidth):
	x = random.randint(0, len(matrix_char)-1)
	line += matrix_char[x]
	index += 1

try:
	while True:
		if index % 5 == 0:
			matrix_char2 = [random.randint(0,mwidth-1) for x in range(10)]
			for i in matrix_char2:
				line[i] = matrix_char[random.randint(0,len(matrix_char)-1)]

		print(*line)
		index += 1
		time.sleep(0.05)

except KeyboardInterrupt:
	pass
		
