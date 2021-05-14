Given the `` root `` of a&nbsp;binary tree, return _the postorder traversal of its nodes' values_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg" style="width: 202px; height: 317px;"/>

<pre>
<strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [3,2,1]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/pre3.jpg" style="width: 202px; height: 197px;"/>

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> [2,1]
</pre>

__Example 5:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/pre2.jpg" style="width: 202px; height: 197px;"/>

<pre>
<strong>Input:</strong> root = [1,null,2]
<strong>Output:</strong> [2,1]
</pre>

&nbsp;

__Constraints:__

*   The number of the nodes in the tree is in the range `` [0, 100] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``

&nbsp;

__Follow up:__

Recursive solution is trivial, could you do it iteratively?

&nbsp;