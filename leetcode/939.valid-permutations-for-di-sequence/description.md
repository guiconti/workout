We are given `` S ``, a length `` n `` string of characters from the set `` {'D', 'I'} ``. (These letters stand for "decreasing" and "increasing".)

A&nbsp;_valid permutation_&nbsp;is a permutation `` P[0], P[1], ..., P[n] `` of integers&nbsp;`` {0, 1, ..., n} ``, such that for all `` i ``:

*   If `` S[i] == 'D' ``, then `` P[i] &gt; P[i+1] ``, and;
*   If `` S[i] == 'I' ``, then `` P[i] &lt; P[i+1] ``.

How many valid permutations are there?&nbsp; Since the answer may be large, __return your answer modulo `` 10^9 + 7 ``__.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">"DID"</span>
<strong>Output: </strong><span id="example-output-1">5</span>
<strong>Explanation: </strong>
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= S.length &lt;= 200 ``
2.   `` S `` consists only of characters from the set `` {'D', 'I'} ``.

<div>
<p>&nbsp;</p>
</div>