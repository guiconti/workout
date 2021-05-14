Given an integer `` n ``, return _a list of all possible __full binary trees__ with_ `` n `` _nodes_. Each node of each tree in the answer must have `` Node.val == 0 ``.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in __any order__.

A __full binary tree__ is a binary tree where each node has exactly `` 0 `` or `` 2 `` children.

&nbsp;

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png" style="width: 700px; height: 400px;"/>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [[0,0,0]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 20 ``