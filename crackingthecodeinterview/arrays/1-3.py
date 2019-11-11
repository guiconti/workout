# Replaces all spaces in a string with %20

# Solution 1 goes through each character in a string if it's a space put a %20
def Solution1(a):
  a = list(a.strip())
  for i in range(len(a)):
    if a[i] == ' ':
      a[i] = '%20'
  return ''.join(a)

if __name__ == '__main__':
  a = 'ab  obo ra ameixa     '
  print(Solution1(a))