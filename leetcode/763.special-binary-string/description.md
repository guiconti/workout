_Special_ binary strings are binary strings with the following two properties:

<li>The number of 0's is equal to the number of 1's.</li><li>Every prefix of the binary string has at least as many 1's as 0's.</li>





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