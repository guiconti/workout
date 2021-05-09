Given the array `` prices `` where `` prices[i] `` is the price of the `` ith `` item in a shop. There is a special discount for items in the shop, if you buy the `` ith `` item, then you will receive a discount equivalent to `` prices[j] `` where `` j `` is the __minimum__&nbsp;index such that `` j &gt; i `` and `` prices[j] &lt;= prices[i] ``, otherwise, you will not receive any discount at all.

_Return an array where the `` ith `` element is the final price you will pay for the `` ith `` item of the shop considering the special discount._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> prices = [8,4,6,2,3]
<strong>Output:</strong> [4,2,4,2,3]
<strong>Explanation:</strong>&nbsp;
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.&nbsp;
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.&nbsp;
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.&nbsp;
For items 3 and 4 you will not receive any discount at all.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> [1,2,3,4,5]
<strong>Explanation:</strong> In this case, for all items, you will not receive any discount at all.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> prices = [10,1,1,6]
<strong>Output:</strong> [9,0,1,6]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= prices.length &lt;= 500 ``
*   `` 1 &lt;= prices[i] &lt;= 10^3 ``