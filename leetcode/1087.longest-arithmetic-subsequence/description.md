Given an array `` A `` of integers, return the __length__ of the longest arithmetic subsequence in `` A ``.

Recall that a _subsequence_ of `` A `` is a list `` A[i_1], A[i_2], ..., A[i_k] `` with `` 0 &lt;= i_1 &lt; i_2 &lt; ... &lt; i_k &lt;= A.length - 1 ``, and that a sequence `` B ``&nbsp;is _arithmetic_ if `` B[i+1] - B[i] `` are all the same value (for `` 0 &lt;= i &lt; B.length - 1 ``).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> A = [3,6,9,12]
<strong>Output:</strong> 4
<strong>Explanation: </strong>
The whole array is an arithmetic sequence with steps of length = 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> A = [9,4,7,2,10]
<strong>Output:</strong> 3
<strong>Explanation: </strong>
The longest arithmetic subsequence is [4,7,10].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> A = [20,1,15,3,10,5,8]
<strong>Output:</strong> 4
<strong>Explanation: </strong>
The longest arithmetic subsequence is [20,15,10,5].
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= A.length &lt;= 1000 ``
*   `` 0 &lt;= A[i] &lt;= 500 ``