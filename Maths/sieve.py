def sieve(n):
	prime=[1]*(n+1)
	prime[0],prime[1]=0,0
	i=2
	while i*i<=n:
		if(prime[i]):
			for j in range(i*i,n+1,i):
				prime[j]=0
		i+=1
	print("Primes are : ")
	for i in range(0,n+1):
		if(prime[i]):
			print(i,end=" ")
	print()

print("Enter upper bound of prime:")
a=int(input())
sieve(a)
