def computeGCD(x, y): 
   while(y): 
       x, y = y, x % y 
  
   return x
   
print("Enter two numbers:")
a,b=map(int,input().split())
print(f"Gcd of {a} and {b} is {computeGCD(a,b)}")
