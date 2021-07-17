def check(n):
	if(n==1):
		return False
	if(n==2 or n==3):
		return True
	i=2
	while i*i<=n:
		if(n%i==0):
			return False
		i+=1
	return True

print("Enter number :")
a=int(input())
if(check(a)):
	print(f"{a} is a prime number")
else:
	print(f"{a} is not a prime number")
