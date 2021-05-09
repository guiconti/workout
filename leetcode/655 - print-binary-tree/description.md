Print a binary tree in an `` m x n `` 2D string array following these rules:

*   The row numbers `` m `` should be equal to the height of the given binary tree.
*   The column number `` n `` should always be an odd number.
*   The root node's value (in string format) should be put in the exact middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (__left-bottom part and right-bottom part__). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
*   Each unused space should contain an empty string `` "" ``.
*   Print the subtrees following the same rules.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/print1-tree.jpg" style="width: 141px; height: 181px;"/>

<pre>
<strong>Input:</strong> root = [1,2]
<strong>Output:</strong> 
[["","1",""],
&nbsp;["2","",""]]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/print2-tree.jpg" style="width: 207px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,null,4]
<strong>Output:</strong> 
[["","","","1","","",""],
&nbsp;["","2","","","","3",""],
&nbsp;["","","4","","","",""]]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 2<sup>10</sup>]</code>.
*   `` -99 &lt;= Node.val &lt;= 99 ``
*   The depth of the tree will be in the range `` [1, 10] ``.