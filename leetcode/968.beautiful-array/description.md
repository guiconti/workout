For some fixed `` N ``, an array `` A `` is _beautiful_ if it is a permutation of the integers `` 1, 2, ..., N ``, such that:

For every `` i &lt; j ``, there is __no__&nbsp;`` k `` with `` i &lt; k &lt; j ``&nbsp;such that `` A[k] * 2 = A[i] + A[j] ``.

Given `` N ``, return __any__ beautiful array `` A ``.&nbsp; (It is guaranteed that one exists.)

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">4</span>
<strong>Output: </strong><span id="example-output-1">[2,1,4,3]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">5</span>
<strong>Output: </strong><span>[3,1,2,5,4]</span></pre>
<p>&nbsp;</p>
</div>

__Note:__

*   `` 1 &lt;= N &lt;= 1000 ``

<div>
<div>&nbsp;</div>
</div>