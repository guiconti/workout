You are given the `` head `` of a linked list, and an integer `` k ``.

Return _the head of the linked list after __swapping__ the values of the _<code>k<sup>th</sup></code> _node from the beginning and the _<code>k<sup>th</sup></code> _node from the end (the list is __1-indexed__)._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg" style="width: 722px; height: 202px;"/>

<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [1,4,3,2,5]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = [7,9,6,6,7,8,3,0,9,5], k = 5
<strong>Output:</strong> [7,9,6,6,8,7,3,0,9,5]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = [1], k = 1
<strong>Output:</strong> [1]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> head = [1,2], k = 1
<strong>Output:</strong> [2,1]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> head = [1,2,3], k = 2
<strong>Output:</strong> [1,2,3]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the list is `` n ``.
*   <code>1 &lt;= k &lt;= n &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= Node.val &lt;= 100 ``