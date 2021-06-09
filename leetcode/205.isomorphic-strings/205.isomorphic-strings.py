class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    hashMap = {}
    cache = set()
    for i in range(len(s)):
      if t[i] in hashMap:
        if hashMap[t[i]] != s[i]:
          return False
        continue
      if s[i] in cache:
        return False
      cache.add(s[i])
      hashMap[t[i]] = s[i]

    return True