n=int(input())

if n%2==0:
	print(((n//2)+1)**2)
elif n%2==1:
	if n==1:
		print(2)
	if n==3:
		print(6)
	else:
		p=n//2
		v1=(p)+1
		v2=p
		print((v1+1)*(v2+1))