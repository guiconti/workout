Strings `` s1 `` and `` s2 `` are `` k ``__-similar__ (for some non-negative integer `` k ``) if we can swap the positions of two letters in `` s1 `` exactly `` k `` times so that the resulting string equals `` s2 ``.

Given two anagrams `` s1 `` and `` s2 ``, return the smallest `` k `` for which `` s1 `` and `` s2 `` are `` k ``__-similar__.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s1 = "ab", s2 = "ba"
<strong>Output:</strong> 1
</pre>

__Example 2:__

<pre><strong>Input:</strong> s1 = "abc", s2 = "bca"
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre><strong>Input:</strong> s1 = "abac", s2 = "baca"
<strong>Output:</strong> 2
</pre>

__Example 4:__

<pre><strong>Input:</strong> s1 = "aabc", s2 = "abca"
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s1.length &lt;= 20 ``
*   `` s2.length == s1.length ``
*   `` s1 `` and `` s2 `` contain only lowercase letters from the set `` {'a', 'b', 'c', 'd', 'e', 'f'} ``.
*   `` s2 `` is an anagram of `` s1 ``.