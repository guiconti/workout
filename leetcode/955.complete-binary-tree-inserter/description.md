A _complete_ binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure&nbsp;`` CBTInserter ``&nbsp;that is initialized with a complete binary tree and supports the following operations:

*   `` CBTInserter(TreeNode root) `` initializes the data structure on a given tree&nbsp;with head node `` root ``;
*   `` CBTInserter.insert(int v) `` will insert a `` TreeNode ``&nbsp;into the tree with value `` node.val =&nbsp;v ``&nbsp;so that the tree remains complete, __and returns the value of the parent of the inserted `` TreeNode ``__;
*   `` CBTInserter.get_root() `` will return the head node of the tree.

<div>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong>inputs = <span id="example-input-1-1">["CBTInserter","insert","get_root"]</span>, inputs = <span id="example-input-1-2">[[[1]],[2],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,1,[1,2]]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>inputs = <span id="example-input-2-1">["CBTInserter","insert","insert","get_root"]</span>, inputs = <span id="example-input-2-2">[[[1,2,3,4,5,6]],[7],[8],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,3,4,[1,2,3,4,5,6,7,8]]</span></pre>
</div>
<div>
<p>&nbsp;</p>
<p><strong>Note:</strong></p>
<ol>
<li>The initial given tree is complete and contains between <code>1</code> and <code>1000</code> nodes.</li>
<li><code>CBTInserter.insert</code> is called at most <code>10000</code> times per test case.</li>
<li>Every value of a given or inserted node is between <code>0</code> and <code>5000</code>.</li>
</ol>
</div>
</div>

<div>
<p>&nbsp;</p>
<div>&nbsp;</div>
</div>