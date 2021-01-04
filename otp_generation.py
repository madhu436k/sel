#from login_Page import *
from random_number import *



c=1
print(a)
for x in range(len(a)):
	b=print(a[x])
print(b)
for i in range(3):
	otp=int(input("enter otp"))
	print()			
	if otp==a[x]:
		print("sucess")
		break
	else:
		print("chance:",c,":plz enter valid otp")
		c+=1
	if c>3:
		print("no more chance")
print()
	

