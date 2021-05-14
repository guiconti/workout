Given a binary tree, return the sum of values of nodes with even-valued grandparent.&nbsp; (A _grandparent_ of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return&nbsp;`` 0 ``.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/07/24/1473_ex1.png" style="width: 350px; height: 214px;"/></strong>

<pre>
<strong>Input:</strong> root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
<strong>Output:</strong> 18
<b>Explanation:</b> The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is between&nbsp;`` 1 ``&nbsp;and&nbsp;`` 10^4 ``.
*   The value of nodes is between&nbsp;`` 1 ``&nbsp;and&nbsp;`` 100 ``.