Given the `` head `` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `` 0 `` until there are no such sequences.

After doing so, return the head of the final linked list.&nbsp; You may return any such answer.

&nbsp;

(Note that in the examples below, all sequences are serializations of `` ListNode `` objects.)

__Example 1:__

<pre>
<strong>Input:</strong> head = [1,2,-3,3,1]
<strong>Output:</strong> [3,1]
<strong>Note:</strong> The answer [1,2,1] would also be accepted.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = [1,2,3,-3,4]
<strong>Output:</strong> [1,2,4]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = [1,2,3,-3,-2]
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   The given linked list will contain between `` 1 `` and `` 1000 `` nodes.
*   Each node in the linked list has `` -1000 &lt;= node.val &lt;= 1000 ``.