Given a non-empty&nbsp;array of unique positive integers `` A ``, consider the following graph:

*   There are `` A.length `` nodes, labelled `` A[0] `` to `` A[A.length - 1]; ``
*   There is an edge between `` A[i] `` and `` A[j] ``&nbsp;if and only if&nbsp;`` A[i] `` and `` A[j] `` share a common factor greater than 1.

Return the size of the largest connected component in the graph.

&nbsp;

<div>
<p><strong>Example 1:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[4,6,15,35]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex1.png" style="width: 257px; height: 50px;"/></span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[20,50,9,63]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex2.png" style="width: 293px; height: 50px;"/></span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-3-1">[2,3,6,7,4,12,21,39]</span>
<strong>Output: </strong><span id="example-output-3">8</span>
<span><img alt="" src="https://assets.leetcode.com/uploads/2018/12/01/ex3.png" style="width: 346px; height: 180px;"/></span>
</pre>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= A.length &lt;= 20000</code></li>
<li><code>1 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
</div>
</div>