Given the `` root `` node of a binary search tree and two integers `` low `` and `` high ``, return _the sum of values of all nodes with a value in the __inclusive__ range _`` [low, high] ``.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg" style="width: 400px; height: 222px;"/>

<pre>
<strong>Input:</strong> root = [10,5,15,3,7,null,18], low = 7, high = 15
<strong>Output:</strong> 32
<strong>Explanation:</strong> Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg" style="width: 400px; height: 335px;"/>

<pre>
<strong>Input:</strong> root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
<strong>Output:</strong> 23
<strong>Explanation:</strong> Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range <code>[1, 2 * 10<sup>4</sup>]</code>.
*   <code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= low &lt;= high &lt;= 10<sup>5</sup></code>
*   All `` Node.val `` are __unique__.