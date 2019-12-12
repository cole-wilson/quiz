import os, time

xc =2

while True:
	xc = (xc + 1)
	print(xc)
	os.system('scrot myscreen' + str(xc) + '.png')
	print('pushing')
	os.system('git add *;git commit * -m "Add Files";git push https://github.com/cole-wilson/quiz master')
	time.sleep(900)
	print('waiting.....\n\n\n\n\...\n\n\n\n')
