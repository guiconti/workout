We are given an array `` A `` of positive integers, and two positive integers `` L `` and `` R `` (`` L &lt;= R ``).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least `` L `` and at most `` R ``.

<pre>
<strong>Example :</strong>
<strong>Input:</strong> 
A = [2, 1, 4, 3]
L = 2
R = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three subarrays that meet the requirements: [2], [2, 1], [3].
</pre>

__Note:__

*   L, R&nbsp; and `` A[i] `` will be an integer in the range `` [0, 10^9] ``.
*   The length of `` A `` will be in the range of `` [1, 50000] ``.