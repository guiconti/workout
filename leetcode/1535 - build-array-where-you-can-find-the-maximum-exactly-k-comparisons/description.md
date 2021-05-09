Given three integers `` n ``, `` m `` and `` k ``. Consider the following algorithm to find the maximum element of an array of positive integers:

<img alt="" src="https://assets.leetcode.com/uploads/2020/04/02/e.png" style="width: 424px; height: 372px;"/>

You should build the array arr which has the following properties:

*   `` arr `` has exactly `` n `` integers.
*   `` 1 &lt;= arr[i] &lt;= m `` where `` (0 &lt;= i &lt; n) ``.
*   After applying the mentioned algorithm to `` arr ``, the value `` search_cost `` is equal to `` k ``.

Return _the number of ways_ to build the array `` arr `` under the mentioned conditions.&nbsp;As the answer may grow large, the answer&nbsp;__must be__&nbsp;computed modulo&nbsp;`` 10^9 + 7 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2, m = 3, k = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 5, m = 2, k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no possible arrays that satisify the mentioned conditions.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 9, m = 1, k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 50, m = 100, k = 25
<strong>Output:</strong> 34549172
<strong>Explanation:</strong> Don't forget to compute the answer modulo 1000000007
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 37, m = 17, k = 7
<strong>Output:</strong> 418930126
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 50 ``
*   `` 1 &lt;= m &lt;= 100 ``
*   `` 0 &lt;= k &lt;= n ``