Given string num representing a non-negative integer `` num ``, and an integer `` k ``, return _the smallest possible integer after removing_ `` k `` _digits from_ `` num ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = "1432219", k = 3
<strong>Output:</strong> "1219"
<strong>Explanation:</strong> Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = "10200", k = 1
<strong>Output:</strong> "200"
<strong>Explanation:</strong> Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = "10", k = 2
<strong>Output:</strong> "0"
<strong>Explanation:</strong> Remove all the digits from the number and it is left with nothing which is 0.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= k &lt;= num.length &lt;= 10<sup>5</sup></code>
*   `` num `` consists of only digits.
*   `` num `` does not have any leading zeros except for the zero itself.