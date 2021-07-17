def linear_search(numbers, target):
	for i in range(len(numbers)):
		if numbers[i] == target:
			return True
	return False




if __name__ == "__main__":
	numbers = [10,30,59,32,12,9,100]
	target = 9 
	result = linear_search(numbers, target)
	if result == True:
		print(f'Target number, {target} is found.')
	else:
		print(f'Target number, {target} is not found.')