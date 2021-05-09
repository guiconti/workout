Given the `` root `` of a binary tree, flatten the tree into a "linked list":

*   The "linked list" should use the same `` TreeNode `` class where the `` right `` child pointer points to the next node in the list and the `` left `` child pointer is always `` null ``.
*   The "linked list" should be in the same order as a <a href="https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR" target="_blank">__pre-order____ traversal__</a> of the binary tree.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" style="width: 500px; height: 226px;"/>

<pre>
<strong>Input:</strong> root = [1,2,5,3,4,null,6]
<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> [0]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 2000] ``.
*   `` -100 &lt;= Node.val &lt;= 100 ``

&nbsp;
__Follow up:__ Can you flatten the tree in-place (with `` O(1) `` extra space)?