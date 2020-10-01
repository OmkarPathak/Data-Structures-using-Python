#inorder to use binary search, numbers should be in sorted order
def binary_search(numbers, target):
	numbers.sort()
	low = 0
	high = len(numbers)-1
	while low <= high:
		mid = low + (high-low)//2
		if numbers[mid] == target:
			return True
		elif numbers[mid] > target:
			high = mid - 1
		else:
			low = mid + 1
	return False




if __name__ == "__main__":
	numbers = [10,30,59,32,12,9,100]
	target = 9 
	result = binary_search(numbers, target)
	if result == True:
		print(f'Target number, {target} is found.')
	else:
		print(f'Target number, {target} is not found.')