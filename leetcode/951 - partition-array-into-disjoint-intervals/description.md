Given an array `` A ``, partition it&nbsp;into two (contiguous) subarrays&nbsp;`` left ``&nbsp;and `` right ``&nbsp;so that:

*   Every element in `` left ``&nbsp;is less than or equal to every element in `` right ``.
*   `` left `` and `` right `` are non-empty.
*   `` left ``&nbsp;has the smallest possible size.

Return the __length__ of `` left `` after such a partitioning.&nbsp; It is guaranteed that such a partitioning exists.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">[5,0,3,8,6]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>left = [5,0,3], right = [8,6]
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1,0,6,12]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation: </strong>left = [1,1,1,0], right = [6,12]
</pre>
<p>&nbsp;</p>
</div>

__Note:__

1.   `` 2 &lt;= A.length&nbsp;&lt;= 30000 ``
2.   `` 0 &lt;= A[i] &lt;= 10^6 ``
3.   It is guaranteed there is at least one way to partition `` A `` as described.

<div>
<div>&nbsp;</div>
</div>