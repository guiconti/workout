Given the `` head `` of a sorted linked list, _delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list_. Return _the linked list __sorted__ as well_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="width: 500px; height: 142px;"/>

<pre>
<strong>Input:</strong> head = [1,2,3,3,4,4,5]
<strong>Output:</strong> [1,2,5]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg" style="width: 500px; height: 205px;"/>

<pre>
<strong>Input:</strong> head = [1,1,1,2,3]
<strong>Output:</strong> [2,3]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the list is in the range `` [0, 300] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``
*   The list is guaranteed to be __sorted__ in ascending order.