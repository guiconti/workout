Given a string `` s ``, the power of the string is the maximum length of a non-empty substring that&nbsp;contains only one unique character.

Return _the power_&nbsp;of the string.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The substring "ee" is of length 2 with the character 'e' only.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "abbcccddddeeeeedcba"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The substring "eeeee" is of length 5 with the character 'e' only.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "triplepillooooow"
<strong>Output:</strong> 5
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "hooraaaaaaaaaaay"
<strong>Output:</strong> 11
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "tourist"
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 500 ``
*   `` s `` contains only lowercase English letters.