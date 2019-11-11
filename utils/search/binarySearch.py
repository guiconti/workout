def binary_search(items, item):
	first = 0
	last = len(items) - 1
	found = False
	while first<=last and not found:
		mid = (first + last) // 2
		if items[mid] == item :
			found = True
		else:
			if item < items[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

if __name__ == '__main__':
  print(binary_search([1,2,3,5,8], 6))
  print(binary_search([1,2,3,5,8], 5))