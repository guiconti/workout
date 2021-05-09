We run a&nbsp;preorder&nbsp;depth-first search (DFS) on the `` root `` of a binary tree.

At each node in this traversal, we output `` D `` dashes (where `` D `` is the depth of this node), then we output the value of this node.&nbsp; If the depth of a node is `` D ``, the depth of its immediate child is `` D + 1 ``.&nbsp; The depth of the `` root `` node is `` 0 ``.

If a node has only one child, that child is guaranteed to be __the left child__.

Given the output `` S `` of this traversal, recover the tree and return _its_ `` root ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/08/recover-a-tree-from-preorder-traversal.png" style="width: 320px; height: 200px;"/>

<pre>
<strong>Input:</strong> S = "1-2--3--4-5--6--7"
<strong>Output:</strong> [1,2,5,3,4,6,7]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114101-pm.png" style="width: 256px; height: 250px;"/>

<pre>
<strong>Input:</strong> S = "1-2--3---4-5--6---7"
<strong>Output:</strong> [1,2,5,3,null,6,null,4,null,7]
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/11/screen-shot-2019-04-10-at-114955-pm.png" style="width: 276px; height: 250px;"/>

<pre>
<strong>Input:</strong> S = "1-401--349---90--88"
<strong>Output:</strong> [1,401,null,349,88,90]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the original tree is in the range `` [1, 1000] ``.
*   <code>1 &lt;= Node.val &lt;= 10<sup>9</sup></code>