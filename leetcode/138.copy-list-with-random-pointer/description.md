A linked list of length `` n `` is given such that each node contains an additional random pointer, which could point to any node in the list, or `` null ``.

Construct a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank">__deep copy__</a> of the list. The deep copy should consist of exactly `` n `` __brand new__ nodes, where each new node has its value set to the value of its corresponding original node. Both the `` next `` and `` random `` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. __None of the pointers in the new list should point to nodes in the original list__.

For example, if there are two nodes `` X `` and `` Y `` in the original list, where `` X.random --&gt; Y ``, then for the corresponding two nodes `` x `` and `` y `` in the copied list, `` x.random --&gt; y ``.

Return _the head of the copied linked list_.

The linked list is represented in the input/output as a list of `` n `` nodes. Each node is represented as a pair of `` [val, random_index] `` where:

*   `` val ``: an integer representing `` Node.val ``
*   `` random_index ``: the index of the node (range from `` 0 `` to `` n-1 ``) that the `` random `` pointer points to, or `` null `` if it does not point to any node.

Your code will __only__ be given the `` head `` of the original linked list.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e1.png" style="width: 700px; height: 142px;"/>

<pre>
<strong>Input:</strong> head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
<strong>Output:</strong> [[7,null],[13,0],[11,4],[10,2],[1,0]]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e2.png" style="width: 700px; height: 114px;"/>

<pre>
<strong>Input:</strong> head = [[1,1],[2,1]]
<strong>Output:</strong> [[1,1],[2,1]]
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/12/18/e3.png" style="width: 700px; height: 122px;"/></strong>

<pre>
<strong>Input:</strong> head = [[3,null],[3,0],[3,null]]
<strong>Output:</strong> [[3,null],[3,0],[3,null]]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
<strong>Explanation:</strong> The given linked list is empty (null pointer), so return null.
</pre>

&nbsp;

__Constraints:__

*   `` 0 &lt;= n &lt;= 1000 ``
*   `` -10000 &lt;= Node.val &lt;= 10000 ``
*   `` Node.random `` is `` null `` or is pointing to some node in the linked list.