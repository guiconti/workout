Given the `` root `` of a binary tree, find the maximum value `` V `` for which there exist __different__ nodes `` A `` and `` B `` where `` V = |A.val - B.val| ``&nbsp;and `` A `` is an ancestor of `` B ``.

A node `` A `` is an ancestor of `` B `` if either: any child of `` A `` is equal to `` B ``, or any child of `` A `` is an ancestor of `` B ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg" style="width: 400px; height: 390px;"/>

<pre>
<strong>Input:</strong> root = [8,3,10,1,6,null,14,null,null,4,7,13]
<strong>Output:</strong> 7
<strong>Explanation: </strong>We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg" style="width: 250px; height: 349px;"/>

<pre>
<strong>Input:</strong> root = [1,null,2,null,0,3]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree&nbsp;is in the range `` [2, 5000] ``.
*   <code>0 &lt;= Node.val &lt;= 10<sup>5</sup></code>