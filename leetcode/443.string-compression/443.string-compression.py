class Solution:
  def compress(self, chars: List[str]) -> int:
    if len(chars) == 0:
      return 0
    answer = []
    previousChar = chars[0]
    count = 0
    for i in range(len(chars)):
      if chars[i] == previousChar:
        count += 1
        continue
      answer.append(previousChar)
      previousChar = chars[i]
      if count == 1:
        continue
      answer.append(str(count))
      count = 1
    answer.append(previousChar)
    if count > 1:
      answer.append(str(count))
    chars = answer
    return len(chars)