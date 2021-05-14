We are given the `` root ``&nbsp;node of a _maximum tree:_ a tree where every node has a value greater than any other value in its subtree.

Just as in the [previous problem](https://leetcode.com/problems/maximum-binary-tree/), the given tree&nbsp;was constructed from an list&nbsp;`` A ``&nbsp;(`` root = Construct(A) ``) recursively with the following&nbsp;`` Construct(A) `` routine:

*   If `` A `` is empty, return `` null ``.
*   Otherwise, let `` A[i] `` be the largest element of `` A ``.&nbsp; Create a `` root `` node with value `` A[i] ``.
*   The left child of `` root `` will be `` Construct([A[0], A[1], ..., A[i-1]]) ``
*   The right child of `` root ``&nbsp;will be `` Construct([A[i+1], A[i+2], ..., A[A.length - 1]]) ``
*   Return `` root ``.

Note that we were not given A directly, only a root node `` root = Construct(A) ``.

Suppose `` B `` is a copy of `` A `` with the value `` val `` appended to it.&nbsp; It is guaranteed that `` B `` has unique values.

Return `` Construct(B) ``.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-1.png" style="width: 159px; height: 160px;"/><img alt="" src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-2.png" style="width: 169px; height: 160px;"/></strong>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[4,1,3,null,null,2]</span>, val = <span id="example-input-1-2">5</span>
<strong>Output: </strong><span id="example-output-1">[5,4,null,1,3,null,null,2]
<strong>Explanation:</strong> A = </span><span>[1,4,2,3], B = </span><span>[1,4,2,3,5]</span>
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-1.png" style="width: 180px; height: 160px;"/><img alt="" src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-2.png" style="width: 214px; height: 160px;"/></strong>

<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[5,2,4,null,1]</span>, val = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">[5,2,4,null,1,null,3]
</span><span id="example-output-1"><strong>Explanation:</strong> A = </span><span>[2,1,5,4], B = </span><span>[2,1,5,4,3]</span>
</pre>

__Example 3:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-1.png" style="width: 180px; height: 160px;"/><img alt="" src="https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-2.png" style="width: 201px; height: 160px;"/></strong>

<pre>
<strong>Input: </strong>root = <span id="example-input-3-1">[5,2,3,null,1]</span>, val = <span id="example-input-3-2">4</span>
<strong>Output: </strong><span id="example-output-3">[5,2,4,null,1,3]
</span><span id="example-output-1"><strong>Explanation:</strong> A = </span><span>[2,1,5,3], B = </span><span>[2,1,5,3,4]</span>
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= B.length &lt;= 100 ``