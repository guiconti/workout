class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    minPrice = 1000000000
    maxProfit = 0
    for price in prices:
      if price < minPrice:
        minPrice = price
        continue
      if (price - minPrice > maxProfit):
        maxProfit = price - minPrice
    return maxProfit