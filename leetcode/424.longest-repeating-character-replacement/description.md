You are given a string `` s `` and an integer `` k ``. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `` k `` times.

Return _the length of the longest substring containing the same letter you can get after performing the above operations_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "ABAB", k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the two 'A's with two 'B's or vice versa.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "AABABBA", k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>5</sup></code>
*   `` s `` consists of only uppercase English letters.
*   `` 0 &lt;= k &lt;= s.length ``