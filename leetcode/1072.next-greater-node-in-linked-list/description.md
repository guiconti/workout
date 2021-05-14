We are given a linked list with&nbsp;`` head ``&nbsp;as the first node.&nbsp; Let's number the&nbsp;nodes in the list: `` node_1, node_2, node_3, ... `` etc.

Each node may have a _next larger_ __value__: for `` node_i ``,&nbsp;`` next_larger(node_i) ``&nbsp;is the `` node_j.val `` such that `` j &gt; i ``, `` node_j.val &gt; node_i.val ``, and `` j `` is the smallest possible choice.&nbsp; If such a `` j ``&nbsp;does not exist, the next larger value is `` 0 ``.

Return an array of integers&nbsp;`` answer ``, where `` answer[i] = next_larger(node_{i+1}) ``.

Note that in the example __inputs__&nbsp;(not outputs) below, arrays such as `` [2,1,5] ``&nbsp;represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,5]</span>
<strong>Output: </strong><span id="example-output-1">[5,5,0]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,7,4,3,5]</span>
<strong>Output: </strong><span id="example-output-2">[7,0,5,5,0]</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,7,5,1,9,2,5,1]</span>
<strong>Output: </strong><span id="example-output-3">[7,9,9,9,0,5,0,0]</span>
</pre>
<p>&nbsp;</p>
<p><strong><span>Note:</span></strong></p>
<ol>
<li><code><span>1 &lt;= node.val&nbsp;&lt;= 10^9</span></code><span>&nbsp;for each node in the linked list.</span></li>
<li>The given list has length in the range <code>[0, 10000]</code>.</li>
</ol>
</div>
</div>
</div>