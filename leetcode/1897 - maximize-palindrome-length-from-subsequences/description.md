You are given two strings, `` word1 `` and `` word2 ``. You want to construct a string in the following manner:

*   Choose some __non-empty__ subsequence `` subsequence1 `` from `` word1 ``.
*   Choose some __non-empty__ subsequence `` subsequence2 `` from `` word2 ``.
*   Concatenate the subsequences: `` subsequence1 + subsequence2 ``, to make the string.

Return _the __length__ of the longest __palindrome__ that can be constructed in the described manner. _If no palindromes can be constructed, return `` 0 ``.

A __subsequence__ of a string `` s `` is a string that can be made by deleting some (possibly none) characters from `` s `` without changing the order of the remaining characters.

A __palindrome__ is a string that reads the same forward&nbsp;as well as backward.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> word1 = "cacb", word2 = "cbba"
<strong>Output:</strong> 5
<strong>Explanation:</strong> Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> word1 = "ab", word2 = "ab"
<strong>Output:</strong> 3
<strong>Explanation:</strong> Choose "ab" from word1 and "a" from word2 to make "aba", which is a palindrome.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> word1 = "aa", word2 = "bb"
<strong>Output:</strong> 0
<strong>Explanation:</strong> You cannot construct a palindrome from the described method, so return 0.</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= word1.length, word2.length &lt;= 1000 ``
*   `` word1 `` and `` word2 `` consist of lowercase English letters.