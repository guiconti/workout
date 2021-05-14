Given the `` root `` of a binary search tree, and an integer `` k ``, return _the_ <code>k<sup>th</sup></code> (__1-indexed__) _smallest element in the tree_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;"/>

<pre>
<strong>Input:</strong> root = [3,1,4,null,2], k = 1
<strong>Output:</strong> 1
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;"/>

<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,null,1], k = 3
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is `` n ``.
*   <code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code>

&nbsp;
__Follow up:__ If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?