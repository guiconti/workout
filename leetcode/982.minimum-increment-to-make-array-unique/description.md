Given an array of integers A, a _move_ consists of choosing any `` A[i] ``, and incrementing it by `` 1 ``.

Return the least number of moves to make every value in `` A `` unique.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,2]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong> After 1 move, the array could be [1, 2, 3].
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><span id="example-input-2-1">[3,2,1,2,1,7]</span>
<strong>Output: </strong><span id="example-output-2">6</span>
<strong>Explanation: </strong> After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
</pre>
<p>&nbsp;</p>
</div>

__Note:__

1.   `` 0 &lt;= A.length &lt;= 40000 ``
2.   `` 0 &lt;= A[i] &lt; 40000 ``

<div>
<div>&nbsp;</div>
</div>