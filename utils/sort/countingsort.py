def count_sort(arr): 
  maxSize = max(arr)
  presence = [0 for x in range(maxSize + 1)]
  for element in arr:
      presence[element] += 1
  for i in range(1,len(presence)):
      presence[i] = presence[i] + presence[i-1]
  b = [0 for x in range(len(arr))]
  for i in range(len(arr)-1,-1,-1):
      b[presence[arr[i]]-1] = arr[i]
      presence[arr[i]] -= 1
  arr = b
  return arr

if __name__ == '__main__':
  test = [5, 7, 6, 2, 1, 7, 3, 0]
  sorted_list = count_sort(test)
  print ('Sorted: ', sorted_list)
