You are given two strings `` s1 `` and `` s2 `` of equal length. A __string swap__ is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return `` true `` _if it is possible to make both strings equal by performing __at most one string swap __on __exactly one__ of the strings. _Otherwise, return `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s1 = "bank", s2 = "kanb"
<strong>Output:</strong> true
<strong>Explanation:</strong> For example, swap the first character with the last character of s2 to make "bank".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s1 = "attack", s2 = "defend"
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make them equal with one string swap.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s1 = "kelb", s2 = "kelb"
<strong>Output:</strong> true
<strong>Explanation:</strong> The two strings are already equal, so no string swap operation is required.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s1 = "abcd", s2 = "dcba"
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s1.length, s2.length &lt;= 100 ``
*   `` s1.length == s2.length ``
*   `` s1 `` and `` s2 `` consist of only lowercase English letters.