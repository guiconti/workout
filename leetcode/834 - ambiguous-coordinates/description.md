We had some 2-dimensional coordinates, like `` "(1, 3)" `` or `` "(2, 0.5)" ``.&nbsp; Then, we removed&nbsp;all commas, decimal points, and spaces, and ended up with the string&nbsp;`` S ``.&nbsp; Return a list of strings representing&nbsp;all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with&nbsp;less digits.&nbsp; Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.&nbsp; Also note that all coordinates in the final answer&nbsp;have exactly one space between them (occurring after the comma.)

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> "(123)"
<strong>Output:</strong> ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> "(00011)"
<strong>Output:</strong> &nbsp;["(0.001, 1)", "(0, 0.011)"]
<strong>Explanation:</strong> 
0.0, 00, 0001 or 00.01 are not allowed.
</pre>

<pre>
<strong>Example 3:</strong>
<strong>Input:</strong> "(0123)"
<strong>Output:</strong> ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
</pre>

<pre>
<strong>Example 4:</strong>
<strong>Input:</strong> "(100)"
<strong>Output:</strong> [(10, 0)]
<strong>Explanation:</strong> 
1.0 is not allowed.
</pre>

&nbsp;

__Note: __

*   `` 4 &lt;= S.length &lt;= 12 ``.
*   `` S[0] `` = "(", `` S[S.length - 1] `` = ")", and the other elements in `` S `` are digits.

&nbsp;