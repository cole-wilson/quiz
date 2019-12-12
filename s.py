import os, time

xc = 6

while True:
	xc = (xc + 1)
	os.system('echo screens: ' + str(xc) + ' > _config.yml') 
	print(xc)
	os.system('scrot myscreen' + str(xc) + '.png')
	print('pushing')
	os.system('git add * >> /dev/null;git commit * -m "Add Files" >> /dev/null;git push https://github.com/cole-wilson/quiz master >> /dev/null')
	time.sleep(900)
	print('waiting.....\n\n\n\n\...\n\n\n\n')
