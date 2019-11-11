# Check if a string is a permutation of a palindrome

# Solution 1 save the amount of characters and check
# if we have an even amount for every character except one if string is even in size O(n)
def Solution1(test):
  dictionary = {}
  for c in test:
    if c in dictionary:
      dictionary[c] += 1
      continue
    if c != ' ':
      dictionary[c] = 1

  oddCount = 0
  for key in dictionary:
    if dictionary[key] % 2 != 0:
      oddCount += 1
  
  return oddCount <= 1

if __name__ == '__main__':
  a = 'ameixaxaemia'
  b = 'atco atc'
  c = 'asamsas'
  print(Solution1(a))
  print(Solution1(b))
  print(Solution1(c))