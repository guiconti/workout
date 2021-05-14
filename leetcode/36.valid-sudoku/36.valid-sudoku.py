class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    sudokuSize = 9
    subBoxSize = 3
    for i in range(sudokuSize):
      # Validate row
      hashmap = collections.defaultdict(bool)
      for cell in board[i]:
        if cell != '.':
          if cell in hashmap:
            return False
          else:
            hashmap[cell] = True
      # Validate columns
      hashmap = collections.defaultdict(bool)
      for cell in board:
        if cell[i] != '.':
          if cell[i] in hashmap:
            return False
          else:
            hashmap[cell[i]] = True
      # Validate sub-box
      hashmap = collections.defaultdict(bool)
      for j in range(subBoxSize):
        rowIndex = j + (subBoxSize * (i // subBoxSize))
        for k in range(subBoxSize):
          columnIndex = k + (subBoxSize * (i % subBoxSize))
          if board[rowIndex][columnIndex] != '.':
            if board[rowIndex][columnIndex] in hashmap:
              return False
            else:
              hashmap[board[rowIndex][columnIndex]] = True
    return True