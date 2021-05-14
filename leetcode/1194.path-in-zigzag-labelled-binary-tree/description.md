In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

<img alt="" src="https://assets.leetcode.com/uploads/2019/06/24/tree.png" style="width: 300px; height: 138px;"/>

Given the `` label `` of a node in this tree, return the labels in the path from the root of the tree to the&nbsp;node with that `` label ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> label = 14
<strong>Output:</strong> [1,3,4,14]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> label = 26
<strong>Output:</strong> [1,2,6,10,26]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= label &lt;= 10^6 ``