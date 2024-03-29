Given an array of integers `` arr ``. Return _the number of sub-arrays_ with __odd__ sum.

As the answer may grow large, the answer&nbsp;__must be__&nbsp;computed modulo&nbsp;`` 10^9 + 7 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,3,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [2,4,6]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,6,7]
<strong>Output:</strong> 16
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [100,100,99,99]
<strong>Output:</strong> 4
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [7]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 10^5 ``
*   `` 1 &lt;= arr[i] &lt;= 100 ``