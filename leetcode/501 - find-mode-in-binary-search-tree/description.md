Given the `` root `` of a binary search tree (BST) with duplicates, return _all the <a href="https://en.wikipedia.org/wiki/Mode_(statistics)" target="_blank">mode(s)</a> (i.e., the most frequently occurred element) in it_.

If the tree has more than one mode, return them in __any order__.

Assume a BST is defined as follows:

*   The left subtree of a node contains only nodes with keys __less than or equal to__ the node's key.
*   The right subtree of a node contains only nodes with keys __greater than or equal to__ the node's key.
*   Both the left and right subtrees must also be binary search trees.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" style="width: 142px; height: 222px;"/>

<pre>
<strong>Input:</strong> root = [1,null,2,2]
<strong>Output:</strong> [2]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> [0]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code>

&nbsp;
__Follow up:__ Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).