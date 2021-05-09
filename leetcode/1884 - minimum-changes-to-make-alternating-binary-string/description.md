You are given a string `` s `` consisting only of the characters `` '0' `` and `` '1' ``. In one operation, you can change any `` '0' `` to `` '1' `` or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string `` "010" `` is alternating, while the string `` "0100" `` is not.

Return _the __minimum__ number of operations needed to make_ `` s `` _alternating_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "0100"
<strong>Output:</strong> 1
<strong>Explanation:</strong> If you change the last character to '1', s will be "0101", which is alternating.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "10"
<strong>Output:</strong> 0
<strong>Explanation:</strong> s is already alternating.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "1111"
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need two operations to reach "0101" or "1010".
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
*   `` s[i] `` is either `` '0' `` or `` '1' ``.