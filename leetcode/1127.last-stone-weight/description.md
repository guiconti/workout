We have a collection of stones, each stone&nbsp;has a positive integer weight.

Each turn, we choose the two __heaviest__&nbsp;stones&nbsp;and smash them together.&nbsp; Suppose the stones have weights `` x `` and `` y `` with `` x &lt;= y ``.&nbsp; The result of this smash is:

*   If `` x == y ``, both stones are totally destroyed;
*   If `` x != y ``, the stone of weight `` x `` is totally destroyed, and the stone of weight `` y `` has new weight `` y-x ``.

At the end, there is at most 1 stone left.&nbsp; Return the weight of this stone (or 0 if there are no stones left.)

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>[2,7,4,1,8,1]
<strong>Output: </strong>1
<strong>Explanation: </strong>
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= stones.length &lt;= 30 ``
2.   `` 1 &lt;= stones[i] &lt;= 1000 ``