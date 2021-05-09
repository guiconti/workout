Given a string `` S `` of lowercase letters, a _duplicate removal_ consists of choosing two adjacent and equal letters, and removing&nbsp;them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.&nbsp; It is guaranteed the answer is unique.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">"abbaca"</span>
<strong>Output: </strong><span id="example-output-1">"ca"</span>
<strong>Explanation: </strong>
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.&nbsp; The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= S.length &lt;= 20000 ``
2.   `` S `` consists only of English lowercase letters.