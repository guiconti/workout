A decimal number is called __deci-binary__ if each of its digits is either `` 0 `` or `` 1 `` without any leading zeros. For example, `` 101 `` and `` 1100 `` are __deci-binary__, while `` 112 `` and `` 3001 `` are not.

Given a string `` n `` that represents a positive decimal integer, return _the __minimum__ number of positive __deci-binary__ numbers needed so that they sum up to _`` n ``_._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = "32"
<strong>Output:</strong> 3
<strong>Explanation:</strong> 10 + 11 + 11 = 32
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = "82734"
<strong>Output:</strong> 8
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = "27346209830709182346"
<strong>Output:</strong> 9
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n.length &lt;= 10<sup>5</sup></code>
*   `` n `` consists of only digits.
*   `` n `` does not contain any leading zeros and represents a positive integer.