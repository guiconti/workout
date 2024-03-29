You are given two __non-empty__ linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg" style="width: 523px; height: 342px;"/>

<pre>
<strong>Input:</strong> l1 = [7,2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,8,0,7]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [8,0,7]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in each linked list is in the range `` [1, 100] ``.
*   `` 0 &lt;= Node.val &lt;= 9 ``
*   It is guaranteed that the list represents a number that does not have leading zeros.

&nbsp;

__Follow up:__&nbsp;Could you solve it without reversing the input lists?