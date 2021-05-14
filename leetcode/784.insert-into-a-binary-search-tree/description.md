You are given the `` root `` node of a binary search tree (BST) and a `` value `` to insert into the tree. Return _the root node of the BST after the insertion_. It is __guaranteed__ that the new value does not exist in the original BST.

__Notice__&nbsp;that there may exist&nbsp;multiple valid ways for the&nbsp;insertion, as long as the tree remains a BST after insertion. You can return __any of them__.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg" style="width: 752px; height: 221px;"/>

<pre>
<strong>Input:</strong> root = [4,2,7,1,3], val = 5
<strong>Output:</strong> [4,2,7,1,3,5]
<strong>Explanation:</strong> Another accepted tree is:
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/bst.jpg" style="width: 352px; height: 301px;"/>
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [40,20,60,10,30,50,70], val = 25
<strong>Output:</strong> [40,20,60,10,30,50,70,null,null,25]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
<strong>Output:</strong> [4,2,7,1,3,5]
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in&nbsp;the tree will be in the range <code>[0,&nbsp;10<sup>4</sup>]</code>.
*   <code>-10<sup>8</sup> &lt;= Node.val &lt;= 10<sup>8</sup></code>
*   All the values `` Node.val `` are __unique__.
*   <code>-10<sup>8</sup> &lt;= val &lt;= 10<sup>8</sup></code>
*   It's __guaranteed__ that `` val `` does not exist in the original BST.