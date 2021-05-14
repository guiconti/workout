Given an array of `` digits `` which is sorted in __non-decreasing__ order. You can write numbers using each `` digits[i] `` as many times as we want. For example, if `` digits = ['1','3','5'] ``, we may write numbers such as `` '13' ``, `` '551' ``, and `` '1351315' ``.

Return _the number of positive integers that can be generated _that are less than or equal to a given integer `` n ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> digits = ["1","3","5","7"], n = 100
<strong>Output:</strong> 20
<strong>Explanation: </strong>
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> digits = ["1","4","9"], n = 1000000000
<strong>Output:</strong> 29523
<strong>Explanation: </strong>
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> digits = ["7"], n = 8
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= digits.length &lt;= 9 ``
*   `` digits[i].length == 1 ``
*   `` digits[i] `` is a digit from&nbsp;`` '1' ``&nbsp;to `` '9' ``.
*   All the values in&nbsp;`` digits `` are __unique__.
*   `` digits `` is sorted in&nbsp;__non-decreasing__ order.
*   <code>1 &lt;= n &lt;= 10<sup>9</sup></code>