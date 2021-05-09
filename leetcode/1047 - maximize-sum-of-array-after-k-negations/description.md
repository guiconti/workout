Given an array `` A `` of integers, we __must__&nbsp;modify the array in the following way: we choose an `` i ``&nbsp;and replace&nbsp;`` A[i] `` with `` -A[i] ``, and we repeat this process `` K `` times in total.&nbsp; (We may choose the same index `` i `` multiple times.)

Return the largest possible sum of the array after modifying it in this way.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[4,2,3]</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">5
<strong>Explanation: </strong>Choose indices (1,) and A becomes [4,-2,3].</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[3,-1,0,2]</span>, K = <span id="example-input-2-2">3</span>
<strong>Output: </strong>6
<span id="example-output-1"><strong>Explanation: </strong>Choose indices (1, 2, 2) and A becomes [3,1,0,2].</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[2,-3,-1,5,-4]</span>, K = <span id="example-input-3-2">2</span>
<strong>Output: </strong><span id="example-output-3">13
</span><span id="example-output-1"><strong>Explanation: </strong>Choose indices (1, 4) and A becomes [2,3,-1,5,4].</span>
</pre>
</div>
</div>

&nbsp;

__Note:__

1.   `` 1 &lt;= A.length &lt;= 10000 ``
2.   `` 1 &lt;= K &lt;= 10000 ``
3.   `` -100 &lt;= A[i] &lt;= 100 ``