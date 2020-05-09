import time
while True:
	arp_file = open('/proc/net/arp','r')
	tamami = arp_file.read()
	satirlar = tamami.split('\n')
	list = []

	for i in satirlar:
		deg = ''
		temp = i.split(' ')
		for j in temp:
			if(j!=''):
				deg = deg+' '+j
		list.append(deg)
	templist = []
	for i in list:
		if(i!=''):
			templist.append(i.split(' '))

	for i in templist:
		for j in templist:
			if(i[1]!=j[1] and i[4]==j[4]):
				print('arp spoof var haciiiiiii!!!!') #buraya saldiri algilandiginda yapilmasi gereken seyleri kod olarak yazabilirsiniz...
	time.sleep(10)
