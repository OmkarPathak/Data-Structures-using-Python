def catalan(n): 
	if (n == 0 or n == 1): 
		return 1
	catalan = [0]*(n+1)
	catalan[0] = 1
	catalan[1] = 1
	for i in range(2, n + 1): 
		catalan[i] = 0
		for j in range(i): 
			catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1] 
	return catalan[n] 

print("Enter value of n:")
a=int(input())
print(f"Catalan Number(nth) is : {catalan(a)}")
