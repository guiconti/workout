class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split(' ')
    if len(words) != len(pattern):
      return
    hashMap = {}
    patternSet = set()
    for i in range(len(words)):
      if words[i] in hashMap:
        if hashMap[words[i]] != pattern[i]:
          return False
      elif pattern[i] in patternSet:
        return False 
      hashMap[words[i]] = pattern[i]
      patternSet.add(pattern[i])
    return True