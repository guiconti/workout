Given the `` root ``&nbsp;of a binary tree, consider all _root to leaf paths_: paths from the root&nbsp;to any leaf.&nbsp; (A leaf is a node with no children.)

A `` node `` is _insufficient_ if&nbsp;__every__ such root to leaf path intersecting this `` node `` has sum strictly less than&nbsp;`` limit ``.

Delete all insufficient nodes simultaneously, and return the root of the resulting&nbsp;binary tree.

&nbsp;

__Example 1:__

<pre>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/06/05/insufficient-11.png" style="width: 482px; height: 200px;"/>
Input: </strong>root = <span id="example-input-1-1">[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]</span>, limit = <span id="example-input-1-2">1</span>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/06/05/insufficient-2.png" style="width: 258px; height: 200px;"/>
Output: </strong><span id="example-output-1">[1,2,3,4,null,null,7,8,9,null,14]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/06/05/insufficient-3.png" style="width: 292px; height: 200px;"/>
Input: </strong>root = <span id="example-input-2-1">[5,4,8,11,null,17,4,7,1,null,null,5,3]</span>, limit = <span id="example-input-2-2">22</span>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/06/05/insufficient-4.png" style="width: 264px; height: 200px;"/>
Output: </strong><span id="example-output-2">[5,4,8,11,null,17,4,7,null,null,null,5]</span></pre>
<p>&nbsp;</p>
<p><strong>Example 3:</strong></p>
<pre>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/06/11/screen-shot-2019-06-11-at-83301-pm.png" style="width: 188px; height: 150px;"/>
Input: </strong>root = <span>[1,2,-3,-5,null,4,null]</span>, limit = -1
<img alt="" src="https://assets.leetcode.com/uploads/2019/06/11/screen-shot-2019-06-11-at-83517-pm.png" style="width: 122px; height: 150px;"/><strong>
Output: </strong><span>[1,null,-3,4]</span></pre>
</div>

&nbsp;

__Note:__

1.   The given tree will have between `` 1 `` and `` 5000 `` nodes.
2.   `` -10^5&nbsp;&lt;= node.val &lt;= 10^5 ``
3.   `` -10^9 &lt;= limit&nbsp;&lt;= 10^9 ``

<div>
<div>&nbsp;</div>
</div>