Given the `` head `` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return _the reordered list_.

The __first__ node is considered __odd__, and the __second__ node is __even__, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg" style="width: 300px; height: 123px;"/>

<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,3,5,2,4]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg" style="width: 500px; height: 142px;"/>

<pre>
<strong>Input:</strong> head = [2,1,3,5,6,4,7]
<strong>Output:</strong> [2,3,6,7,1,5,4]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the linked list is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>6</sup> &lt;= Node.val &lt;= 10<sup>6</sup></code>

&nbsp;
__Follow up:__ Could you solve it in `` O(1) `` space complexity and `` O(nodes) `` time complexity?