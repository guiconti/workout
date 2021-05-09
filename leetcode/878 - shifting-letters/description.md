We have a string `` S `` of lowercase letters, and an integer array `` shifts ``.

Call the _shift_ of a letter, the next letter in the alphabet, (wrapping around so that `` 'z' `` becomes `` 'a' ``).&nbsp;

For example, `` shift('a') = 'b' ``, `` shift('t') = 'u' ``, and `` shift('z') = 'a' ``.

Now for each `` shifts[i] = x ``, we want to shift the first `` i+1 ``&nbsp;letters of `` S ``, `` x `` times.

Return the final string&nbsp;after all such shifts to `` S `` are applied.

__Example 1:__

<pre>
<strong>Input: </strong>S = "abc", shifts = [3,5,9]
<strong>Output: </strong>"rpl"
<strong>Explanation: </strong>
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
</pre>

__Note:__

1.   `` 1 &lt;= S.length = shifts.length &lt;= 20000 ``
2.   `` 0 &lt;= shifts[i] &lt;= 10 ^ 9 ``