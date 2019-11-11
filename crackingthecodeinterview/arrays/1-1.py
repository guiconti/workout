# Implement an unique algorithm to determine if a string has all unique characters. What if you could not implement
# additional data structures

# Solution 1 with additional data structures (hash table) O(n)
def Solution1(test):
  dictionary = {}

  for c in test:
    if c in dictionary:
      return False
    dictionary[c] = True
  return True

# Solution 2 with no additional data structures (sort then check) O(nlogn + n)
def Solution2(test):
  test = ''.join(sorted(test))
  for i in range(len(test) - 1):
    if test[i] == test[i + 1]:
      return False
  return True



if __name__ == '__main__':
  test1 = 'abcdefg'
  test2 = 'abcdefgha'
  print(Solution1(test1))
  print(Solution1(test2))
  print(Solution2(test1))
  print(Solution2(test2))