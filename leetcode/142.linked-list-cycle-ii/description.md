Given a linked list, return the node where the cycle begins. If there is no cycle, return `` null ``.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the&nbsp;`` next ``&nbsp;pointer. Internally, `` pos ``&nbsp;is used to denote the index of the node that&nbsp;tail's&nbsp;`` next ``&nbsp;pointer is connected to.&nbsp;__Note that&nbsp;`` pos ``&nbsp;is not passed as a parameter__.

__Notice__ that you __should not modify__ the linked list.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="height: 145px; width: 450px;"/>

<pre>
<strong>Input:</strong> head = [3,2,0,-4], pos = 1
<strong>Output:</strong> tail connects to node index 1
<strong>Explanation:</strong> There is a cycle in the linked list, where tail connects to the second node.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 105px; width: 201px;"/>

<pre>
<strong>Input:</strong> head = [1,2], pos = 0
<strong>Output:</strong> tail connects to node index 0
<strong>Explanation:</strong> There is a cycle in the linked list, where tail connects to the first node.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 65px; width: 65px;"/>

<pre>
<strong>Input:</strong> head = [1], pos = -1
<strong>Output:</strong> no cycle
<strong>Explanation:</strong> There is no cycle in the linked list.
</pre>

&nbsp;

__Constraints:__

*   The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code>
*   `` pos `` is `` -1 `` or a __valid index__ in the linked-list.

&nbsp;

__Follow up:__ Can you solve it using `` O(1) `` (i.e. constant) memory?