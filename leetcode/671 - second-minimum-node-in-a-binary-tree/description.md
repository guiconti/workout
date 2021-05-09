Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly `` two `` or `` zero `` sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property&nbsp;`` root.val = min(root.left.val, root.right.val) ``&nbsp;always holds.

Given such a binary tree, you need to output the __second minimum__ value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

&nbsp;
&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg" style="width: 431px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [2,2,5,null,null,5,7]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The smallest value is 2, the second smallest value is 5.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg" style="width: 321px; height: 182px;"/>

<pre>
<strong>Input:</strong> root = [2,2,2]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The smallest value is 2, but there isn't any second smallest value.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 25] ``.
*   <code>1 &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code>
*   `` root.val == min(root.left.val, root.right.val) ``&nbsp;for each internal node of the tree.