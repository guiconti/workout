Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

>  
> a binary tree in which the left and right subtrees of _every_ node differ in height by no more than 1.
> 
&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;"/>

<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;"/>

<pre>
<strong>Input:</strong> root = [1,2,2,3,3,null,null,4,4]
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [0, 5000] ``.
*   <code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code>