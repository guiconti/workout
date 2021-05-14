Given an&nbsp;array&nbsp;of __distinct__&nbsp;integers `` arr ``, find all pairs of elements with the minimum absolute difference of any two elements.&nbsp;

Return a list of pairs in ascending order(with respect to pairs), each pair `` [a, b] `` follows

*   `` a, b `` are from `` arr ``
*   `` a &lt; b ``
*   `` b - a ``&nbsp;equals to the minimum absolute difference of any two elements in `` arr ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [4,2,1,3]
<strong>Output:</strong> [[1,2],[2,3],[3,4]]
<strong>Explanation: </strong>The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,3,6,10,15]
<strong>Output:</strong> [[1,3]]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [3,8,-10,23,19,-4,-14,27]
<strong>Output:</strong> [[-14,-10],[19,23],[23,27]]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= arr.length &lt;= 10^5 ``
*   `` -10^6 &lt;= arr[i] &lt;= 10^6 ``