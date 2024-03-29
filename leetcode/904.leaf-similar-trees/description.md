Consider all the leaves of a binary tree, from&nbsp;left to right order, the values of those&nbsp;leaves form a __leaf value sequence___._

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" style="width: 400px; height: 336px;"/>

For example, in the given tree above, the leaf value sequence is `` (6, 7, 4, 9, 8) ``.

Two binary trees are considered _leaf-similar_&nbsp;if their leaf value sequence is the same.

Return `` true `` if and only if the two given trees with head nodes `` root1 `` and `` root2 `` are leaf-similar.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg" style="width: 750px; height: 297px;"/>

<pre>
<strong>Input:</strong> root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root1 = [1], root2 = [1]
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root1 = [1], root2 = [2]
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root1 = [1,2], root2 = [2,2]
<strong>Output:</strong> true
</pre>

__Example 5:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg" style="width: 450px; height: 165px;"/>

<pre>
<strong>Input:</strong> root1 = [1,2,3], root2 = [1,3,2]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in each tree will be in the range `` [1, 200] ``.
*   Both of the given trees will have values in the range `` [0, 200] ``.