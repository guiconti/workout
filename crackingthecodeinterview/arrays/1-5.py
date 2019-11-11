# There are three types of edits in string. Insert a char, remove a char or replace a char
# Given two string find out if they are one or less edits aways

# Solution 1 check their sizes. If they have the same size check for a replace edit
# if their size is no greater than 1 check for an insert edit O(N)
def Solution1(a, b):

  if len(a) == len(b):
    return checkForEdit(a, b)
  if len(a) - 1 == len(b):
    return checkForInsert(a, b)
  if len(b) - 1 == len(a):
    return checkForInsert(b, a)
  return False

def checkForEdit(a, b):
  editFound = False
  
  for i in range(len(a)):
    if a[i] != b[i]:
      if editFound:
        return False
      editFound = True
  
  return True

def checkForInsert(a, b):
  indexA = 0
  indexB = 0

  while indexA < len(a) and indexB < len(b):
    if a[indexA] != b[indexB]:
      if indexA != indexB:
        return False
      if len(a) > len(b):
        indexA += 1
      else:
        indexB += 1
    else:
      indexA += 1
      indexB += 1

  return True
  

if __name__ == '__main__':
  a = 'ameixa'
  b = 'ameixb'
  print(Solution1(a, b))