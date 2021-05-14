A binary tree is _univalued_ if every node in the tree has the same value.

Return `` true ``&nbsp;if and only if the given tree is univalued.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png" style="width: 265px; height: 172px;"/>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,1,1,1,1,null,1]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png" style="width: 198px; height: 169px;"/>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,2,2,5,2]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>
</div>

&nbsp;

__Note:__

1.   The number of nodes in the given tree will be in the range `` [1, 100] ``.
2.   Each node's value will be an integer in the range `` [0, 99] ``.