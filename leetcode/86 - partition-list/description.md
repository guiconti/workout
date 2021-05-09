Given the `` head `` of a linked list and a value `` x ``, partition it such that all nodes __less than__ `` x `` come before nodes __greater than or equal__ to `` x ``.

You should __preserve__ the original relative order of the nodes in each of the two partitions.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" style="width: 662px; height: 222px;"/>

<pre>
<strong>Input:</strong> head = [1,4,3,2,5,2], x = 3
<strong>Output:</strong> [1,2,2,4,3,5]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = [2,1], x = 2
<strong>Output:</strong> [1,2]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the list is in the range `` [0, 200] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``
*   `` -200 &lt;= x &lt;= 200 ``