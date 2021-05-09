Return the number of __distinct__ non-empty substrings of `` text ``&nbsp;that can be written as the concatenation of some string with itself (i.e. it can be written as `` a + a ``&nbsp;where `` a `` is some string).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> text = "abcabcabc"
<strong>Output:</strong> 3
<b>Explanation: </b>The 3 substrings are "abcabc", "bcabca" and "cabcab".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> text = "leetcodeleetcode"
<strong>Output:</strong> 2
<b>Explanation: </b>The 2 substrings are "ee" and "leetcodeleetcode".
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= text.length &lt;= 2000 ``
*   `` text ``&nbsp;has only lowercase English letters.