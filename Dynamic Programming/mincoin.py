import sys

def min_coins(coins,sum): 
      
    # dp[i] will be storing the minimum 
    dp = [0 for i in range(sum + 1)] 
  
    # Base case
    dp[0] = 0
  
    # Initialize values as Infinite 
    for i in range(1, sum + 1): 
      dp[i] = sys.maxsize 
    
    # for all values from 1 to sum
    for i in range(1, sum + 1): 
      for j in range(len(coins)): 
        if (coins[j] <= i): 
          res = dp[i - coins[j]] 
          if (res != sys.maxsize and res + 1 < dp[i]): 
            dp[i] = res + 1
    return dp[sum] 
  
 
if __name__ == "__main__": 
    coins = [9, 6, 5, 1] 
    m = len(coins) 
    amount = 11
    print("Minimum coins:",min_coins(coins,amount)) 