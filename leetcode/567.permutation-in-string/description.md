Given two strings `` s1 `` and `` s2 ``, return true if `` s2 `` contains the permutation of `` s1 ``.

In other words, one of `` s1 ``'s permutations is the substring of `` s2 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s1 = "ab", s2 = "eidbaooo"
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 ("ba").
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s1 = "ab", s2 = "eidboaoo"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code>
*   `` s1 `` and `` s2 `` consist of lowercase English letters.