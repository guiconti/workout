from typing import Hashable


class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    hashMap = {}
    for character in s:
      if not character in hashMap:
        hashMap[character] = 0
      hashMap[character] += 1
    for character in t:
      if not character in hashMap:
        return False
      if hashMap[character] <= 0:
        return False
      hashMap[character] -= 1
    return True