Given a binary tree `` root ``.&nbsp;Split the binary tree into two subtrees by removing&nbsp;1 edge such that the product of the sums of the subtrees are maximized.

Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;10^9 + 7.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png" style="width: 495px; height: 200px;"/></strong>

<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6]
<strong>Output:</strong> 110
<strong>Explanation:</strong> Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png" style="width: 495px; height: 200px;"/>

<pre>
<strong>Input:</strong> root = [1,null,2,3,4,null,null,5,6]
<strong>Output:</strong> 90
<strong>Explanation:</strong>  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [2,3,9,10,7,8,6,5,4,11,1]
<strong>Output:</strong> 1025
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [1,1]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   Each tree has at most `` 50000 `` nodes and at least `` 2 `` nodes.
*   Each node's value is between `` [1, 10000] ``.