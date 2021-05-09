In an array `` A `` containing only 0s and 1s, a _`` K ``-bit flip&nbsp;_consists of choosing a (contiguous) subarray of length `` K `` and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of `` K ``-bit flips required so that there is no 0 in the array.&nbsp; If it is not possible, return `` -1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[0,1,0]</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>Flip A[0], then flip A[2].
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,1,0]</span>, K = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation:</strong>&nbsp;No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[0,0,0,1,0,1,1,0]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation:</strong>
Flip A[0],A[1],A[2]:&nbsp;A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]:&nbsp;A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]:&nbsp;A becomes [1,1,1,1,1,1,1,1]
</pre>
<p>&nbsp;</p>
</div>
</div>

__Note:__

1.   `` 1 &lt;= A.length &lt;=&nbsp;30000 ``
2.   `` 1 &lt;= K &lt;= A.length ``