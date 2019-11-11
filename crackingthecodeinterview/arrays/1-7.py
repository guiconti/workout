# Given an image represented by NXN matrix where each pixel is 4 bytes
# Write a method to rotate it in 90 degress. Can you do it in place

# Solution 1 Iterate through the string and while the next is equals to the current
# increment your current sum, when you found a different string append your result
# and restart your count O(n)
def Solution1(test):
  if len(test) == 0 or len(test) != len(test[0]):
    return False
  
  n = len(test)

  for i in range(n // 2):
    first = i
    last = n - 1 - i
    for j in range(first, last):
      offset = j - first
      
      top = test[first][j]
      test[first][j] = test[last - offset][first]
      test[last - offset][first] = test[last][last - offset]
      test[last][last - offset] = test[j][last]
      test[j][last] = top
  
  return test

if __name__ == '__main__':
  a = [ 
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
      ]
  print(Solution1(a))