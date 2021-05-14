Given a string `` s `` and an integer `` k ``, return _the length of the longest substring of_ `` s `` _such that the frequency of each character in this substring is greater than or equal to_ `` k ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "aaabb", k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest substring is "aaa", as 'a' is repeated 3 times.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "ababbc", k = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
*   `` s `` consists of only lowercase English letters.
*   <code>1 &lt;= k &lt;= 10<sup>5</sup></code>