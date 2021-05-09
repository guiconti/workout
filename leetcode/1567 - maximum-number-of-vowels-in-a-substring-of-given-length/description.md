Given a string `` s `` and an integer `` k ``.

Return _the maximum number of vowel letters_ in any substring of `` s ``&nbsp;with&nbsp;length `` k ``.

__Vowel letters__ in&nbsp;English are&nbsp;(a, e, i, o, u).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abciiidef", k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring "iii" contains 3 vowel letters.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aeiou", k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Any substring of length 2 contains 2 vowels.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "leetcode", k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> "lee", "eet" and "ode" contain 2 vowels.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "rhythms", k = 4
<strong>Output:</strong> 0
<strong>Explanation:</strong> We can see that s doesn't have any vowel letters.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "tryhard", k = 4
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``
*   `` s ``&nbsp;consists of lowercase English letters.
*   `` 1 &lt;= k &lt;= s.length ``