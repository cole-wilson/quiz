import os, time

xc =0

while True:
	xc = (xc + 1)
	print(xc)
	os.system('scrot myscreen' + str(xc) + '.png')
	time.sleep(1800)
