# Sorting Type: Radix
# 
# Description: Radix sort is a sorting technique that
# sorts the elements by first grouping the individual
# digits of same place value. Then, sort the elements
# according to their increasing/decreasing order.

from math import log10
from random import randint

def get_num(num, base, pos):
  return (num // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixsort(l, base=10):
  passes = int(log10(max(l))+1)
  output = [0] * len(l)

  for pos in range(passes):
    count = [0] * base

    for i in l:
      digit = get_num(i, base, pos)
      count[digit] +=1

    count = prefix_sum(count)

    for i in reversed(l):
      digit = get_num(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i

    l = list(output)
  return output

l = [ randint(1, 99999) for x in range(100) ]
sorted = radixsort(l)
print(sorted)
