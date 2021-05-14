Given a string `` s `` and an integer `` k ``, reverse the first `` k `` characters for every `` 2k `` characters counting from the start of the string.

If there are fewer than `` k `` characters left, reverse all of them. If there are less than `` 2k `` but greater than or equal to `` k `` characters, then reverse the first `` k `` characters and left the other as original.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> s = "abcdefg", k = 2
<strong>Output:</strong> "bacdfeg"
</pre>

__Example 2:__

<pre><strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "bacd"
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
*   `` s `` consists of only lowercase English letters.
*   <code>1 &lt;= k &lt;= 10<sup>4</sup></code>