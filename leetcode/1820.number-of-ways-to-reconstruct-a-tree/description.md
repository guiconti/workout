You are given an array `` pairs ``, where <code>pairs[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>, and:

*   There are no duplicates.
*   <code>x<sub>i</sub> &lt; y<sub>i</sub></code>

Let `` ways `` be the number of rooted trees that satisfy the following conditions:

*   The tree consists of nodes whose values appeared in `` pairs ``.
*   A pair <code>[x<sub>i</sub>, y<sub>i</sub>]</code> exists in `` pairs `` __if and only if__ <code>x<sub>i</sub></code> is an ancestor of <code>y<sub>i</sub></code> or <code>y<sub>i</sub></code> is an ancestor of <code>x<sub>i</sub></code>.
*   __Note:__ the tree does not have to be a binary tree.

Two ways are considered to be different if there is at least one node that has different parents in both ways.

Return:

*   `` 0 `` if `` ways == 0 ``
*   `` 1 `` if `` ways == 1 ``
*   `` 2 `` if `` ways &gt; 1 ``

A __rooted tree__ is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

An __ancestor__ of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.

&nbsp;

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2020/12/03/trees2.png" style="width: 208px; height: 221px;"/>

<pre>
<strong>Input:</strong> pairs = [[1,2],[2,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is exactly one valid rooted tree, which is shown in the above figure.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/03/tree.png" style="width: 234px; height: 241px;"/>

<pre>
<strong>Input:</strong> pairs = [[1,2],[2,3],[1,3]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are multiple valid rooted trees. Three of them are shown in the above figures.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> pairs = [[1,2],[2,3],[2,4],[1,5]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no valid rooted trees.</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= pairs.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= x<sub>i </sub>&lt; y<sub>i</sub> &lt;= 500</code>
*   The elements in `` pairs `` are unique.