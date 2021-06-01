class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    s1 = sorted(s1)
    candidate = ''
    for i in range(len(s2) - len(s1) + 1):
      if i == 0:
        candidate = sorted(s2[i:i + len(s1)])
      else:
        candidate = candidate[1:]

      if s1 == candidate:
        return True
    return False

    # Theres a better way where we store the occurences in a 26 sized array
    # Then duplicate the array on every try and see if it matches.