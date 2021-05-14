We write the integers of `` A `` and `` B ``&nbsp;(in the order they are given) on two separate horizontal lines.

Now, we may draw _connecting lines_: a straight line connecting two numbers `` A[i] `` and `` B[j] ``&nbsp;such that:

*   `` A[i] == B[j] ``;
*   The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints:&nbsp;each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/04/26/142.png" style="width: 100px; height: 72px;"/>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,4,2]</span>, B = <span id="example-input-1-2">[1,2,4]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[2,5,1,2,5]</span>, B = <span id="example-input-2-2">[10,5,2,1,5,2]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[1,3,7,1,7,5]</span>, B = <span id="example-input-3-2">[1,9,2,5,1]</span>
<strong>Output: </strong><span id="example-output-3">2</span></pre>
<p>&nbsp;</p>
</div>
</div>

__Note:__

<ol><li><code>1 &lt;= A.length &lt;= 500</code></li><li><code>1 &lt;= B.length &lt;= 500</code></li><li><code><font face="monospace">1 &lt;= A[i], B[i] &lt;= 2000</font></code></li></ol>