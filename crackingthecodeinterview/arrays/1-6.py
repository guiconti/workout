# Implement a method for compression on string like aabbbbcdd a2b4c1d2
# If the result is bigger than the original string return the original string

# Solution 1 Iterate through the string and while the next is equals to the current
# increment your current sum, when you found a different string append your result
# and restart your count O(n)
def Solution1(test):
  currentCount = 1
  result = ''

  for i in range(len(test)):
    if i < len(test) - 1 and test[i] == test[i + 1]:
      currentCount += 1
    else:
      result += test[i] + str(currentCount)
      currentCount = 1

    if len(result) >= len(test):
      return test
  
  return result


if __name__ == '__main__':
  a = 'abccdd'
  print(Solution1(a))