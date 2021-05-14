Given a linked list, reverse the nodes of a linked list _k_ at a time and return its modified list.

_k_ is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of _k_ then left-out nodes, in the end, should remain as it is.

You may&nbsp;not alter the values in the list's nodes, only nodes themselves may be changed.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 542px; height: 222px;"/>

<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [2,1,4,3,5]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" style="width: 542px; height: 222px;"/>

<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 3
<strong>Output:</strong> [3,2,1,4,5]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 1
<strong>Output:</strong> [1,2,3,4,5]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> head = [1], k = 1
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the list&nbsp;is in the range `` sz ``.
*   `` 1 &lt;= sz &lt;= 5000 ``
*   `` 0 &lt;= Node.val &lt;= 1000 ``
*   `` 1 &lt;= k &lt;= sz ``

&nbsp;
__Follow-up:__ Can you solve the problem in O(1) extra memory space?