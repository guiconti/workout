You have `` n `` binary tree nodes numbered from `` 0 `` to `` n - 1 `` where node `` i `` has two children `` leftChild[i] `` and `` rightChild[i] ``, return `` true `` if and only if __all__ the given nodes form __exactly one__ valid binary tree.

If node `` i `` has no left child then `` leftChild[i] `` will equal `` -1 ``, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex1.png" style="width: 195px; height: 287px;"/>

<pre>
<strong>Input:</strong> n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex2.png" style="width: 183px; height: 272px;"/>

<pre>
<strong>Input:</strong> n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
<strong>Output:</strong> false
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex3.png" style="width: 82px; height: 174px;"/>

<pre>
<strong>Input:</strong> n = 2, leftChild = [1,0], rightChild = [-1,-1]
<strong>Output:</strong> false
</pre>

__Example 4:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/08/23/1503_ex4.png" style="width: 470px; height: 191px;"/>

<pre>
<strong>Input:</strong> n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   `` leftChild.length == rightChild.length == n ``
*   `` -1 &lt;= leftChild[i], rightChild[i] &lt;= n - 1 ``