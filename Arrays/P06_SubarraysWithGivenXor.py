def subarrays_with_given_XOR(arr, n, m):
    prefix_xor = 0
    
    d = {0: 1}  # initialise dictionary, d stores count 'xor values' in arr
    for i in range(n):
        prefix_xor ^= arr[i]
        if prefix_xor in d: 
            d[prefix_xor] += 1
        else: 
            d[prefix_xor] = 1
    
    # Approach :
      # We know that, If A^B = C, then: A^C=B and B^C=A,
      
      # In this problem :-
      
      # val ^ givenXor = C
      # givenXor ^ c = a
      # val ^ c = givenXor
      # So, if val and val^givenXor=C is in d, then "givenXor" is in d.
    

    cnt = 0
    for val in d:
        if val^m in d:
            cnt += d[val] * d[val^m]
            d[e] = 0
            d[val^m] = 0
    return cnt


arr = [4, 2, 2, 6, 4]
xor = 6
print(subarrays_with_given_XOR(arr, len(arr), xor))
