# Given an image represented by NXN matrix where each pixel is 4 bytes
# Write a method to rotate it in 90 degress. Can you do it in place

# Solution 1 The easiest way to do this is to implement the rotation in layers.
# We perform a circular rotation on each layer, moving the top edge to the right edge, the right edge 
# to the bottom edge, the bottom edge to the left edge, and the left edge to the top edge
# We perform such a swap on each layer, starting from the outermost layer and working our way inwards.
def Solution1(test):
  if len(test) == 0 or len(test) != len(test[0]):
    return False
  
  n = len(test)

  for i in range(n // 2):
    first = i
    last = n - 1 - i
    for j in range(first, last):
      # Essentially the column
      offset = j - first
      
      # Save top
      top = test[first][j]
      # Left to top
      test[first][j] = test[last - offset][first]
      # Bottom to left
      test[last - offset][first] = test[last][last - offset]
      # Right to Bottom
      test[last][last - offset] = test[j][last]
      # Top to right
      test[j][last] = top
  
  return test

if __name__ == '__main__':
  a = [ 
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
      ]
  print(Solution1(a))