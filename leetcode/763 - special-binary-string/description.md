_Special_ binary strings are binary strings with the following two properties:

<li>The number of 0's is equal to the number of 1's.</li><li>Every prefix of the binary string has at least as many 1's as 0's.</li>

Given a special string `` S ``, a _move_ consists of choosing two consecutive, non-empty, special substrings of `` S ``, and swapping them. _(Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)_

At the end of any number of moves, what is the lexicographically largest resulting string possible?

__Example 1:__  

<pre>
<b>Input:</b> S = "11011000"
<b>Output:</b> "11100100"
<b>Explanation:</b>
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
</pre>

__Note:__

1.   `` S `` has length at most `` 50 ``.
2.   `` S `` is guaranteed to be a _special_ binary string as defined above.