Given a binary search tree, return a __balanced__ binary search tree with the same node values.

A binary search tree is _balanced_ if and only if&nbsp;the depth of the two subtrees of&nbsp;every&nbsp;node never differ by more than 1.

If there is more than one answer, return any of them.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/08/22/1515_ex1.png" style="width: 250px; height: 248px;"/><img alt="" src="https://assets.leetcode.com/uploads/2019/08/22/1515_ex1_out.png" style="width: 200px; height: 200px;"/></strong>

<pre>
<strong>Input:</strong> root = [1,null,2,null,3,null,4,null,null]
<strong>Output:</strong> [2,1,3,null,null,null,4]
<b>Explanation:</b> This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is between&nbsp;`` 1 ``&nbsp;and&nbsp;`` 10^4 ``.
*   The tree nodes will have distinct values between&nbsp;`` 1 ``&nbsp;and&nbsp;`` 10^5 ``.