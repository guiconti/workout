Given two strings `` s `` and `` p ``, return _an array of all the start indices of _`` p ``_'s anagrams in _`` s ``. You may return the answer in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "cbaebabacd", p = "abc"
<strong>Output:</strong> [0,6]
<strong>Explanation:</strong>
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "abab", p = "ab"
<strong>Output:</strong> [0,1,2]
<strong>Explanation:</strong>
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length, p.length &lt;= 3 * 10<sup>4</sup></code>
*   `` s `` and `` p `` consist of lowercase English letters.