Given the `` root `` of a&nbsp;binary tree, return _the lowest common ancestor of its deepest leaves_.

Recall that:

*   The node of a binary tree is a leaf if and only if it has no children
*   The depth of the root of the tree is `` 0 ``. if the depth of a node is `` d ``, the depth of each of its children&nbsp;is&nbsp;`` d + 1 ``.
*   The lowest common ancestor of a set `` S `` of nodes, is the node `` A `` with the largest depth such that every node in `` S `` is in the subtree with root `` A ``.

__Note:__ This question is the same as 865: <a href="https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/" target="_blank">https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/</a>

&nbsp;

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png" style="width: 600px; height: 510px;"/>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4]
<strong>Output:</strong> [2,7,4]
<strong>Explanation:</strong> We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The root is the deepest node in the tree, and it's the lca of itself.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [0,1,3,null,2]
<strong>Output:</strong> [2]
<strong>Explanation:</strong> The deepest leaf node in the tree is 2, the lca of one node is itself.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree will be in the range `` [1, 1000] ``.
*   `` 0 &lt;= Node.val &lt;= 1000 ``
*   The values of the nodes in the tree&nbsp;are __unique__.