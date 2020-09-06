import random, threading

def threadings():
	for x in range(0, 350):
		t = threading.Thread(target=making)
		t.start()

def making():
	ip = str(random.randint(1,255)) + '.' + str(random.randint(1, 255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(1, 255))
	a = ''
	rand = random.randint(1, 25)
	for i in range(rand):
		a += '###'
	f = open('hosts.txt', 'a+')
	f.write(str( a + ' ' + ip + " growtopia1.com\n" + ip + ' growtopia2.com\n'))
	f.close()
	
threadings()

#(C) Made By KIPAS#1823
