Given the `` root `` of a binary tree, construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/cons1-tree.jpg" style="width: 292px; height: 301px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,4]
<strong>Output:</strong> "1(2(4))(3)"
<strong>Explanation:</strong> Originallay it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/cons2-tree.jpg" style="width: 207px; height: 293px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,null,4]
<strong>Output:</strong> "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
*   `` -1000 &lt;= Node.val &lt;= 1000 ``