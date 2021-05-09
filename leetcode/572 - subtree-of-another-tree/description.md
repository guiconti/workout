Given the roots of two binary trees `` root `` and `` subRoot ``, return `` true `` if there is a subtree of `` root `` with the same structure and node values of``  subRoot `` and `` false `` otherwise.

A subtree of a binary tree `` tree `` is a tree that consists of a node in `` tree `` and all of this node's descendants. The tree `` tree `` could also be considered as a subtree of itself.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg" style="width: 532px; height: 400px;"/>

<pre>
<strong>Input:</strong> root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg" style="width: 502px; height: 458px;"/>

<pre>
<strong>Input:</strong> root = [3,4,5,1,2,null,null,0], subRoot = [4,1,2]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the `` root `` tree is in the range `` [1, 2000] ``.
*   The number of nodes in the `` subRoot `` tree is in the range `` [1, 1000] ``.
*   <code>-10<sup>4</sup> &lt;= root.val &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> &lt;= subRoot.val &lt;= 10<sup>4</sup></code>