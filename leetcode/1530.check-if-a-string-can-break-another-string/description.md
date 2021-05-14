Given two strings: `` s1 `` and `` s2 `` with the same&nbsp;size, check if some&nbsp;permutation of string `` s1 `` can break&nbsp;some&nbsp;permutation of string `` s2 `` or vice-versa. In other words `` s2 `` can break `` s1 ``&nbsp;or vice-versa.

A string `` x ``&nbsp;can break&nbsp;string `` y ``&nbsp;(both of size `` n ``) if `` x[i] &gt;= y[i] ``&nbsp;(in alphabetical order)&nbsp;for all `` i ``&nbsp;between `` 0 `` and `` n-1 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s1 = "abc", s2 = "xya"
<strong>Output:</strong> true
<strong>Explanation:</strong> "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s1 = "abe", s2 = "acd"
<strong>Output:</strong> false 
<strong>Explanation:</strong> All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s1 = "leetcodee", s2 = "interview"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` s1.length == n ``
*   `` s2.length == n ``
*   `` 1 &lt;= n &lt;= 10^5 ``
*   All strings consist of lowercase English letters.