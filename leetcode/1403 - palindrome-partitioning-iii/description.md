You are given a string&nbsp;`` s `` containing lowercase letters and an integer `` k ``. You need to :

*   First, change some characters of `` s ``&nbsp;to other lowercase English letters.
*   Then divide `` s ``&nbsp;into `` k `` non-empty disjoint substrings such that each substring is palindrome.

Return the minimal number of characters that you need to change&nbsp;to divide the string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abc", k = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong>&nbsp;You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aabbc", k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;You can split the string into "aa", "bb" and "c", all of them are palindrome.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "leetcode", k = 8
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;= s.length &lt;= 100 ``.
*   `` s ``&nbsp;only contains lowercase English letters.