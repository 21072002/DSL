a=input('name of employee: ')
b=int(input('designation\n 1. manager\n 2. Team leader\n 3. team member\n Enter designation:  '))
if b==1:
	day=int(input('enter the no of working days : '))
	if day<=31:
		sl=(day*2000)
		print('salary of manager in working days is ',sl)
		ext=int(input('enter the no of overtime: '))
		slb=((day+ext)*2000)
		print('total salary is ',slb)
	else:
		print('error')
elif b==2:
	day=int(input('enter no working of days'))
	if day<=31:
		sl=(day*1800)
		print('salary of Team leader is ', sl)
		ext=int(input('enter no of overtime'))
		sbl=((day+ext)*1800)
		print('total salary is ',slb)
	else:
		print('error')
elif b==3:
	day=int(input('enter no of working days: '))
	if day<=31:
		sl=(day*1500)
		print('salary of Team member is',sl)
		ext=int(input('enter no of overtime'))
		sbl=((day+ext)*1500)
		print('total salary is ',sbl)
	else:
		print('error')
else:
	print('error')
	
	
