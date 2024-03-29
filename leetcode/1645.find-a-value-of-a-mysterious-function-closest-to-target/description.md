<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/change.png" style="width: 635px; height: 312px;"/>

Winston was given the above mysterious function `` func ``. He has an integer array `` arr `` and an integer `` target `` and he wants to find the values `` l `` and `` r `` that make the value `` |func(arr, l, r) - target| `` minimum possible.

Return _the minimum possible value_ of `` |func(arr, l, r) - target| ``.

Notice that `` func `` should be called with the values `` l `` and `` r `` where `` 0 &lt;= l, r &lt; arr.length ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [9,12,3,7,15], target = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> Calling func with all the pairs of [l,r] = [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]], Winston got the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0]. The value closest to 5 is 7 and 3, thus the minimum difference is 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1000000,1000000,1000000], target = 1
<strong>Output:</strong> 999999
<strong>Explanation:</strong> Winston called the func with all possible values of [l,r] and he always got 1000000, thus the min difference is 999999.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,2,4,8,16], target = 0
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= arr[i] &lt;= 10<sup>6</sup></code>
*   <code>0 &lt;= target &lt;= 10<sup>7</sup></code>