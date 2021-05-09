Given a list of __unique__ words, return all the pairs of the&nbsp;___distinct___ indices `` (i, j) `` in the given list, so that the concatenation of the two words&nbsp;`` words[i] + words[j] `` is a palindrome.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> words = ["abcd","dcba","lls","s","sssll"]
<strong>Output:</strong> [[0,1],[1,0],[3,2],[2,4]]
<strong>Explanation:</strong> The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> words = ["bat","tab","cat"]
<strong>Output:</strong> [[0,1],[1,0]]
<strong>Explanation:</strong> The palindromes are ["battab","tabbat"]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> words = ["a",""]
<strong>Output:</strong> [[0,1],[1,0]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= words.length &lt;= 5000 ``
*   `` 0 &lt;= words[i].length &lt;= 300 ``
*   `` words[i] `` consists of lower-case English letters.