For a binary tree __T__, we can define a __flip operation__ as follows: choose any node, and swap the left and right child subtrees.

A binary tree __X__&nbsp;is _flip equivalent_ to a binary tree __Y__ if and only if we can make __X__ equal to __Y__ after some number of flip operations.

Given the roots of two binary trees `` root1 `` and `` root2 ``, return `` true `` if the two trees are flip equivelent or `` false `` otherwise.

&nbsp;

__Example 1:__

<img alt="Flipped Trees Diagram" src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png" style="width: 500px; height: 220px;"/>

<pre>
<strong>Input:</strong> root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
<strong>Output:</strong> true
<strong>Explanation: </strong>We flipped at nodes with values 1, 3, and 5.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root1 = [], root2 = []
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root1 = [], root2 = [1]
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root1 = [0,null,1], root2 = []
<strong>Output:</strong> false
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> root1 = [0,null,1], root2 = [0,1]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in each tree is in the range `` [0, 100] ``.
*   Each tree will have __unique node values__ in the range `` [0, 99] ``.