<code data-stringify-type="code">n</code>&nbsp;passengers board an airplane with exactly&nbsp;<code data-stringify-type="code">n</code>&nbsp;seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of passengers will:

*   Take their own seat if it is still available,&nbsp;
*   Pick other seats randomly when they find their seat occupied&nbsp;

What is the probability that the n-th person can get his own seat?

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1.00000
<strong>Explanation: </strong>The first person can only get the first seat.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 0.50000
<strong>Explanation: </strong>The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^5 ``