Given a __non-empty__ array of decimal digits&nbsp;representing a non-negative integer, increment&nbsp;one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> digits = [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> digits = [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> digits = [0]
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= digits.length &lt;= 100 ``
*   `` 0 &lt;= digits[i] &lt;= 9 ``