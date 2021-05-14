Given two equal-size strings `` s `` and `` t ``. In one step you can choose __any character__ of `` t `` and replace it with __another character__.

Return _the minimum number of steps_ to make `` t ``&nbsp;an anagram of `` s ``.

An&nbsp;__Anagram__&nbsp;of a&nbsp;string&nbsp;is a string that contains the same characters with a different (or the same) ordering.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "bab", t = "aba"
<strong>Output:</strong> 1
<strong>Explanation:</strong> Replace the first 'a' in t with b, t = "bba" which is anagram of s.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "leetcode", t = "practice"
<strong>Output:</strong> 5
<strong>Explanation:</strong> Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "anagram", t = "mangaar"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "anagram" and "mangaar" are anagrams. 
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "xxyyzz", t = "xxyyzz"
<strong>Output:</strong> 0
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "friend", t = "family"
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 50000 ``
*   `` s.length == t.length ``
*   `` s `` and `` t `` contain lower-case English letters only.