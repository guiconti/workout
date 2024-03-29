In a row of trees, the `` i ``-th tree&nbsp;produces&nbsp;fruit with type&nbsp;`` tree[i] ``.

You __start at any tree&nbsp;of your choice__, then repeatedly perform the following steps:

1.   Add one piece of fruit from this tree to your baskets.&nbsp; If you cannot, stop.
2.   Move to the next tree to the right of the current tree.&nbsp; If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree:&nbsp;you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,1]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong><span>Explanation: </span></strong><span>We can collect [1,2,1].</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,1,2,2]</span>
<strong>Output: </strong><span id="example-output-2">3
</span><strong><span>Explanation: </span></strong><span>We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,2,3,2,2]</span>
<strong>Output: </strong><span id="example-output-3">4
</span><strong><span>Explanation: </span></strong><span>We can collect [2,3,2,2].</span>
<span>If we started at the first tree, we would only collect [1, 2].</span>
</pre>
<div>
<p><strong>Example 4:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,3,3,1,2,1,1,2,3,3,4]</span>
<strong>Output: </strong>5<span id="example-output-4">
</span><strong><span>Explanation: </span></strong><span>We can collect [1,2,1,1,2].</span>
<span>If we started at the first tree or the eighth tree, we would only collect 4 fruits.</span>
</pre>
<p>&nbsp;</p>
</div>
</div>
</div>

__Note:__

1.   `` 1 &lt;= tree.length &lt;= 40000 ``
2.   `` 0 &lt;= tree[i] &lt; tree.length ``