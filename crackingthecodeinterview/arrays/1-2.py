# Given two strings check if one is a permutation of the other

# Solution 1 sort the strings and check if they match O(2 * nlogn)
def Solution1(a, b):
  a = ''.join(sorted(a))
  b = ''.join(sorted(b))

  return a == b

# Solution 2 assuming it's ASCII we create an array that will hold the count of each character
def Solution2(a, b):
  if len(a) != len(b):
    return False
  ASCIIList = [0] * 128
  for c in a:
    ASCIIList[ord(c)] += 1
  for c in b:
    ASCIIList[ord(c)] -= 1
    if (ASCIIList[ord(c)] < 0):
      return False
  return True

if __name__ == '__main__':
  a = 'aboboraameixa'
  b = 'aameixboboara'
  c = 'goddog'
  d = 'gooddog'
  print(Solution1(a, b))
  print(Solution1(c, d))
  print(Solution2(a, b))
  print(Solution2(c, d))