Given a string `` s `` and an integer `` k ``. You should construct `` k `` non-empty __palindrome__ strings using __all the characters__ in `` s ``.

Return ___True___ if you can use all the characters in `` s `` to construct `` k `` palindrome strings or ___False___ otherwise.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "annabelle", k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "leetcode", k = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to construct 3 palindromes using all the characters of s.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "true", k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> The only possible solution is to put each character in a separate string.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "yzyzyzyzyzyzyzy", k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "cr", k = 7
<strong>Output:</strong> false
<strong>Explanation:</strong> We don't have enough characters in s to construct 7 palindromes.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   All characters in `` s `` are lower-case English letters.
*   `` 1 &lt;= k &lt;= 10^5 ``