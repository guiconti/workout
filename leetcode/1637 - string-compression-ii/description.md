[Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding) is a string compression method that works by&nbsp;replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string&nbsp;`` "aabccc" ``&nbsp;we replace 

<font face="monospace"><code>"aa"</code></font>

&nbsp;by&nbsp;

<font face="monospace"><code>"a2"</code></font>

&nbsp;and replace 

<font face="monospace"><code>"ccc"</code></font>

&nbsp;by&nbsp;

<font face="monospace"><code>"c3"</code></font>

. Thus the compressed string becomes 

<font face="monospace"><code>"a2bc3"</code>.</font>

Notice that in this problem, we are not adding&nbsp;`` '1' ``&nbsp;after single characters.

Given a&nbsp;string `` s ``&nbsp;and an integer `` k ``. You need to delete __at most__&nbsp;`` k `` characters from&nbsp;`` s ``&nbsp;such that the run-length encoded version of `` s ``&nbsp;has minimum length.

Find the _minimum length of the run-length encoded&nbsp;version of _`` s ``_ after deleting at most _`` k ``_ characters_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aaabcccd", k = 2
<strong>Output:</strong> 4
<b>Explanation: </b>Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "aabbaa", k = 2
<strong>Output:</strong> 2
<b>Explanation: </b>If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "aaaaaaaaaaa", k = 0
<strong>Output:</strong> 3
<strong>Explanation: </strong>Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 100 ``
*   `` 0 &lt;= k &lt;= s.length ``
*   `` s `` contains only lowercase English letters.