#wapp to find fact of a number

def fact(num):
	f=1
	for i in range(1,num+1):
		f=f*i
	return f
number=int(input("Enter a number"))
if number<0:
	print("b+ve")
elif number==0 or number==1:
	print("fact=",1)
else:
	ans=fact(number)
	print("fact=",ans)