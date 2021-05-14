Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain __at least__ three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits `` '0'-'9' ``, write a function to determine if it's an additive number.

__Note:__ Numbers in the additive sequence __cannot__ have leading zeros, so sequence `` 1, 2, 03 `` or `` 1, 02, 3 `` is invalid.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> "112358"
<strong>Output:</strong> true
<strong>Explanation:</strong> The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
&nbsp;            1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> "199100199"
<strong>Output:</strong> true
<strong>Explanation:</strong> The additive sequence is: 1, 99, 100, 199.&nbsp;
&nbsp;            1 + 99 = 100, 99 + 100 = 199
</pre>

&nbsp;

__Constraints:__

<ul><li><font face="monospace"><code>num</code>&nbsp;</font>consists only of digits <code>'0'-'9'</code>.</li><li><code>1 &lt;= num.length &lt;= 35</code></li></ul>

__Follow up:__  
How would you handle overflow for very large input integers?