Given a string `` s ``. In one step you can insert any character at any index of the string.

Return _the minimum number of steps_ to make `` s ``&nbsp;palindrome.

A&nbsp;__Palindrome String__&nbsp;is one that reads the same backward as well as forward.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "zzazz"
<strong>Output:</strong> 0
<strong>Explanation:</strong> The string "zzazz" is already palindrome we don't need any insertions.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "mbadm"
<strong>Output:</strong> 2
<strong>Explanation:</strong> String can be "mbdadbm" or "mdbabdm".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> 5
<strong>Explanation:</strong> Inserting 5 characters the string becomes "leetcodocteel".
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "g"
<strong>Output:</strong> 0
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "no"
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 500 ``
*   All characters of `` s ``&nbsp;are lower case English letters.