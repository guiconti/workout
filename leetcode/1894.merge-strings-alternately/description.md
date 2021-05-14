You are given two strings `` word1 `` and `` word2 ``. Merge the strings by adding letters in alternating order, starting with `` word1 ``. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return _the merged string._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word1 = "abc", word2 = "pqr"
<strong>Output:</strong> "apbqcr"
<strong>Explanation:</strong>&nbsp;The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word1 = "ab", word2 = "pqrs"
<strong>Output:</strong> "apbqrs"
<strong>Explanation:</strong>&nbsp;Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> word1 = "abcd", word2 = "pq"
<strong>Output:</strong> "apbqcd"
<strong>Explanation:</strong>&nbsp;Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= word1.length, word2.length &lt;= 100 ``
*   `` word1 `` and `` word2 `` consist of lowercase English letters.