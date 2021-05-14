Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1.   Search for a node to remove.
2.   If the node is found, delete the node.

__Follow up:__&nbsp;Can you solve it with time complexity `` O(height of tree) ``?

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg" style="width: 800px; height: 214px;"/>

<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 3
<strong>Output:</strong> [5,4,6,2,null,null,7]
<strong>Explanation:</strong> Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg" style="width: 350px; height: 255px;"/>
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,7], key = 0
<strong>Output:</strong> [5,3,6,2,4,null,7]
<strong>Explanation:</strong> The tree does not contain a node with value = 0.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [], key = 0
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code>
*   Each node has a __unique__ value.
*   `` root `` is a valid binary search tree.
*   <code>-10<sup>5</sup> &lt;= key &lt;= 10<sup>5</sup></code>