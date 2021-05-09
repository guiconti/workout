Given a string S, find the number of different non-empty palindromic subsequences in S, and __return that number modulo `` 10^9 + 7 ``.__

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences `` A_1, A_2, ... `` and `` B_1, B_2, ... `` are different if there is some `` i `` for which `` A_i != B_i ``.

__Example 1:__  

<pre>
<b>Input:</b> 
S = 'bccb'
<b>Output:</b> 6
<b>Explanation:</b> 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
</pre>

__Example 2:__  

<pre>
<b>Input:</b> 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
<b>Output:</b> 104860361
<b>Explanation:</b> 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
</pre>

__Note:__<li>The length of <code>S</code> will be in the range <code>[1, 1000]</code>.</li><li>Each character <code>S[i]</code> will be in the set <code>{'a', 'b', 'c', 'd'}</code>.</li>