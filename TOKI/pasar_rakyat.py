def multiply_arr(arr):
	result = 1
	for i in range(len(arr)):
		result *= arr[i]
	return result
 
def pasar_rakyat(test_case):
	arr = []
	index = 0

	for i in range(test_case):
		arr.append(int(input()))

	arr.sort()
	trial = multiply_arr(arr)//arr[0]
	for i in range(1, trial+1):
		smallest = arr[0] * i
		for j in range(1, len(arr)):
			if smallest % arr[j] != 0:
				break
			elif smallest % arr[j] == 0 and j == len(arr)-1:
				index = i
				break
			else:
				continue
		if i == index:
			break
	return smallest

if __name__ == '__main__':
	trial = int(input())
	print(pasar_rakyat(trial))