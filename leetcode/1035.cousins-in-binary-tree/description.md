In a binary tree, the root node is at depth `` 0 ``, and children of each depth `` k `` node are at depth `` k+1 ``.

Two nodes of a binary tree are _cousins_ if they have the same depth, but have __different parents__.

We are given the `` root `` of a binary tree with unique values, and the values `` x ``&nbsp;and `` y ``&nbsp;of two different nodes in the tree.

Return&nbsp;`` true ``&nbsp;if and only if the nodes corresponding to the values `` x `` and `` y `` are cousins.

&nbsp;

<strong>Example 1:<br/><img alt="" src="https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png" style="width: 180px; height: 160px;"/></strong>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[1,2,3,4]</span>, x = <span id="example-input-1-2">4</span>, y = <span id="example-input-1-3">3</span>
<strong>Output: </strong><span id="example-output-1">false</span>
</pre>

<div>
<p><strong>Example 2:<br/>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png" style="width: 201px; height: 160px;"/></strong></p>
<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[1,2,3,null,4,null,5]</span>, x = <span id="example-input-2-2">5</span>, y = <span id="example-input-2-3">4</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png" style="width: 156px; height: 160px;"/></strong></p>
<pre>
<strong>Input: </strong>root = <span id="example-input-3-1">[1,2,3,null,4]</span>, x = 2, y = 3
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>
</div>
</div>

&nbsp;

__Constraints:__

*   The number of nodes in the tree will be between `` 2 `` and `` 100 ``.
*   Each node has a unique integer value from `` 1 `` to `` 100 ``.