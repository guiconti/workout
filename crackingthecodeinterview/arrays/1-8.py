# Write an algorithm such that if an element in a matrix MXN is 0, its entire row and column will be 0
# If the result is bigger than the original string return the original string

# Solution 1 Iterate through each element, if a 0 is found add it's row and column to two
# support arrays. After everything is checked use the additional arrays to override the
# rows and columns with 0s
def Solution1(test):
  rows = [False] * len(test)
  columns = [False] * len(test[0])

  for i in range(len(test)):
    for j in range(len(test[i])):
      if test[i][j] == 0:
        rows[i] = True
        columns[j] = True

  for i in range(len(rows)):
    if rows[i]:
      for j in range(len(test[i])):
        test[i][j] = 0

  for i in range(len(columns)):
    if columns[i]:
      for j in range(len(test)):
        test[j][i] = 0

  return test


if __name__ == '__main__':
  a = [ 
      [1, 2, 3],
      [4, 0, 6],
      [7, 8, 9]
    ]
  print(Solution1(a))