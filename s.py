import os, time

xc =0

while True:
	xc = (xc + 1)
	print(xc)
	os.system('scrot myscreen' + str(xc) + '.png')
	time.sleep(1)
	if xc % 1 == 0:
		print('pushing')
		os.system('git add *;git commit * -m "Add Files";git push https://github.com/cole-wilson/quiz')
