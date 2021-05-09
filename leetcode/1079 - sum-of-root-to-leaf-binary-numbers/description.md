You are given the `` root `` of a binary tree where each node has a value `` 0 ``&nbsp;or `` 1 ``.&nbsp; Each root-to-leaf path represents a binary number starting with the most significant bit.&nbsp; For example, if the path is `` 0 -&gt; 1 -&gt; 1 -&gt; 0 -&gt; 1 ``, then this could represent `` 01101 `` in binary, which is `` 13 ``.

For all leaves in the tree, consider the numbers represented by the path&nbsp;from the root to that leaf.

Return _the sum of these numbers_. The answer is __guaranteed__ to fit in a __32-bits__ integer.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png" style="width: 450px; height: 296px;"/>

<pre>
<strong>Input:</strong> root = [1,0,1,0,1,0,1]
<strong>Output:</strong> 22
<strong>Explanation: </strong>(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> 0
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [1,1]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the tree is in the range `` [1, 1000] ``.
*   `` Node.val `` is `` 0 `` or `` 1 ``.