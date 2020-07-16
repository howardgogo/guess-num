import random
r = random.randint(1 , 100)
r = int(r)
while True:
	p = input('請猜一個數字')
	p = int(p)#p放在迴圈裡才會重複問
	if (p) == (r) :
		print('終於猜對了!')
		break
	else:
		if p > r:
			print('比答案大')
		else:
			print('比答案小')


