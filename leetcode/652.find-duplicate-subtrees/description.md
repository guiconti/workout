Given the `` root ``&nbsp;of a binary tree, return all __duplicate subtrees__.

For each kind of duplicate subtrees, you only need to return the root node of any __one__ of them.

Two trees are __duplicate__ if they have the __same structure__ with the __same node values__.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e1.jpg" style="width: 450px; height: 354px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,4,null,2,4,null,null,4]
<strong>Output:</strong> [[2,4],[4]]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e2.jpg" style="width: 321px; height: 201px;"/>

<pre>
<strong>Input:</strong> root = [2,1,1]
<strong>Output:</strong> [[1]]
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e33.jpg" style="width: 450px; height: 303px;"/>

<pre>
<strong>Input:</strong> root = [2,2,2,3,null,3,null]
<strong>Output:</strong> [[2,3],[3]]
</pre>

&nbsp;

__Constraints:__

*   The number of the nodes in the tree will be in the range `` [1, 10^4] ``
*   `` -200 &lt;= Node.val &lt;= 200 ``