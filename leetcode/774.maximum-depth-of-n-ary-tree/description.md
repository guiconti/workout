Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

_Nary-Tree input serialization&nbsp;is represented in their level order traversal, each group of children is separated by the null value (See examples)._

&nbsp;

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;"/>

<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> 3
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;"/>

<pre>
<strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   The depth of the n-ary tree is less than or equal to `` 1000 ``.
*   The total number of nodes is between <code>[0,&nbsp;10<sup>4</sup>]</code>.