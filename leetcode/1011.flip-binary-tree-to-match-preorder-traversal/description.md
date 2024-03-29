You are given the `` root `` of a binary tree with `` n `` nodes, where each node is uniquely assigned a value from `` 1 `` to `` n ``. You are also given a sequence of `` n `` values `` voyage ``, which is the __desired__ <a href="https://en.wikipedia.org/wiki/Tree_traversal#Pre-order" target="_blank">__pre-order traversal__</a> of the binary tree.

Any node in the binary tree can be __flipped__ by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/15/fliptree.jpg" style="width: 400px; height: 187px;"/>

Flip the __smallest__ number of nodes so that the __pre-order traversal__ of the tree __matches__ `` voyage ``.

Return _a list of the values of all __flipped__ nodes. You may return the answer in __any order__. If it is __impossible__ to flip the nodes in the tree to make the pre-order traversal match _`` voyage ``_, return the list _`` [-1] ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-01.png" style="width: 150px; height: 205px;"/>

<pre>
<strong>Input:</strong> root = [1,2], voyage = [2,1]
<strong>Output:</strong> [-1]
<strong>Explanation:</strong> It is impossible to flip the nodes such that the pre-order traversal matches voyage.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 150px; height: 142px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3], voyage = [1,3,2]
<strong>Output:</strong> [1]
<strong>Explanation:</strong> Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 150px; height: 142px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3], voyage = [1,2,3]
<strong>Output:</strong> []
<strong>Explanation:</strong> The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is `` n ``.
*   `` n == voyage.length ``
*   `` 1 &lt;= n &lt;= 100 ``
*   `` 1 &lt;= Node.val, voyage[i] &lt;= n ``
*   All the values in the tree are __unique__.
*   All the values in `` voyage `` are __unique__.