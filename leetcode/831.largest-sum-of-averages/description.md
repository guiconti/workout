We partition a row of numbers `` A ``&nbsp;into at most `` K `` adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 
A = [9,1,2,3,9]
K = 3
<strong>Output:</strong> 20
<strong>Explanation:</strong> 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
</pre>

&nbsp;

__Note: __

*   `` 1 &lt;= A.length &lt;= 100 ``.
*   `` 1 &lt;= A[i] &lt;= 10000 ``.
*   `` 1 &lt;= K &lt;= A.length ``.
*   Answers within `` 10^-6 `` of the correct answer will be accepted as correct.