We are given a binary tree (with root node&nbsp;`` root ``), a `` target `` node, and an integer value `` K ``.

Return a list of the values of all&nbsp;nodes that have a distance `` K `` from the `` target `` node.&nbsp; The answer can be returned in any order.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[3,5,1,6,2,0,8,null,null,7,4]</span>, target = <span id="example-input-1-2">5</span>, K = <span id="example-input-1-3">2</span>

<strong>Output: </strong><span id="example-output-1">[7,4,1]</span>

<strong>Explanation: </strong>
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="width: 280px; height: 240px;"/>

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
</pre>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li>The given tree is non-empty.</li>
<li>Each node in the tree has unique values&nbsp;<code>0 &lt;= node.val &lt;= 500</code>.</li>
<li>The <code>target</code>&nbsp;node is a node in the tree.</li>
<li><code>0 &lt;= K &lt;= 1000</code>.</li>
</ol>
</div>