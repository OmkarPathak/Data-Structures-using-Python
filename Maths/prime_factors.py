def prime_factors(n):
	i=2
	ans=[]
	while i*i<=n:
		if(n%i==0):
			ans.append(i)
			while(n%i==0):
				n=n//i
		i+=1
	if(n!=1):
		ans.append(n)
	if(len(ans)==0):
		print("No prime factors")
	else:
		print("Prime factors are : ",end=" ")
		print(*ans)


print("Enter number:")
a=int(input())
prime_factors(a)
