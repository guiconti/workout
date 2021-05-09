Given the `` root `` of a binary search tree and the lowest and highest boundaries as `` low `` and `` high ``, trim the tree so that all its elements lies in `` [low, high] ``. Trimming the tree should __not__ change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a __unique answer__.

Return _the root of the trimmed binary search tree_. Note that the root may change depending on the given bounds.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg" style="width: 450px; height: 126px;"/>

<pre>
<strong>Input:</strong> root = [1,0,2], low = 1, high = 2
<strong>Output:</strong> [1,null,2]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg" style="width: 450px; height: 277px;"/>

<pre>
<strong>Input:</strong> root = [3,0,4,null,2,null,null,1], low = 1, high = 3
<strong>Output:</strong> [3,2,null,1]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [1], low = 1, high = 2
<strong>Output:</strong> [1]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [1,null,2], low = 1, high = 3
<strong>Output:</strong> [1,null,2]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> root = [1,null,2], low = 2, high = 4
<strong>Output:</strong> [2]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code>
*   The value of each node in the tree is __unique__.
*   `` root `` is guaranteed to be a valid binary search tree.
*   <code>0 &lt;= low &lt;= high &lt;= 10<sup>4</sup></code>