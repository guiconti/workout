Given an array of&nbsp;integers `` arr `` and an integer `` d ``. In one step you can jump from index `` i `` to index:

*   `` i + x `` where:&nbsp;`` i + x &lt; arr.length `` and ``  0 &lt;&nbsp;x &lt;= d ``.
*   `` i - x `` where:&nbsp;`` i - x &gt;= 0 `` and ``  0 &lt;&nbsp;x &lt;= d ``.

In addition, you can only jump from index `` i `` to index `` j ``&nbsp;if `` arr[i] &gt; arr[j] `` and `` arr[i] &gt; arr[k] `` for all indices `` k `` between `` i `` and `` j `` (More formally `` min(i,&nbsp;j) &lt; k &lt; max(i, j) ``).

You can choose any index of the array and start jumping. Return _the maximum number of indices_&nbsp;you can visit.

Notice that you can not jump outside of the array at any time.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/23/meta-chart.jpeg" style="width: 633px; height: 419px;"/>

<pre>
<strong>Input:</strong> arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can start at index 10. You can jump 10 --&gt; 8 --&gt; 6 --&gt; 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 &gt; 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 &gt; 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [3,3,3,3,3], d = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> You can start at any index. You always cannot jump to any index.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [7,6,5,4,3,2,1], d = 1
<strong>Output:</strong> 7
<strong>Explanation:</strong> Start at index 0. You can visit all the indicies. 
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [7,1,7,1,7,1], d = 2
<strong>Output:</strong> 2
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [66], d = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 1000 ``
*   `` 1 &lt;= arr[i] &lt;= 10^5 ``
*   `` 1 &lt;= d &lt;= arr.length ``