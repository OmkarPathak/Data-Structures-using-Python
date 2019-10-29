def lds(arr, n): 
  
    lds = [0] * n 
    max = 0
  
    # Initialize LDS with 1 for all index 
    # The minimum LDS starting with any 
    # element is always 1 
    for i in range(n): 
        lds[i] = 1
  
    # Compute LDS from every index 
    # in bottom up manner 
    for i in range(1, n): 
        for j in range(i): 
            if (arr[i] < arr[j] and 
                lds[i] < lds[j] + 1): 
                lds[i] = lds[j] + 1
  
    # Select the maximum  
    # of all the LDS values 
    for i in range(n): 
        if (max < lds[i]): 
            max = lds[i] 
  
    # returns the length of the LDS 
    return max
