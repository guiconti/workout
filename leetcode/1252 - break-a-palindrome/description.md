Given a palindromic string of lowercase English letters `` palindrome ``, replace __exactly one__ character with any lowercase English letter so that the resulting string is __not__ a palindrome and that it is the __lexicographically smallest__ one possible.

Return _the resulting string. If there is no way to replace a character to make it not a palindrome, return an __empty string__._

A string `` a `` is lexicographically smaller than a string `` b `` (of the same length) if in the first position where `` a `` and `` b `` differ, `` a `` has a character strictly smaller than the corresponding character in `` b ``. For example, `` "abcc" `` is lexicographically smaller than `` "abcd" `` because the first position they differ is at the fourth character, and `` 'c' `` is smaller than `` 'd' ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> palindrome = "abccba"
<strong>Output:</strong> "aaccba"
<strong>Explanation:</strong> There are many ways to make "abccba" not a palindrome, such as "<u>z</u>bccba", "a<u>a</u>ccba", and "ab<u>a</u>cba".
Of all the ways, "aaccba" is the lexicographically smallest.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> palindrome = "a"
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> palindrome = "aa"
<strong>Output:</strong> "ab"</pre>

__Example 4:__

<pre>
<strong>Input:</strong> palindrome = "aba"
<strong>Output:</strong> "abb"
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= palindrome.length &lt;= 1000 ``
*   `` palindrome `` consists of only lowercase English letters.