A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits and all we know is that all integers in the array were in the range&nbsp;`` [1, k] ``&nbsp;and there are no leading zeros in the array.

Given the string `` s `` and the integer `` k ``. There can be multiple ways to restore the array.

Return _the number of possible array_ that can be printed as a string `` s ``&nbsp;using the mentioned program.

The number of ways could be very large so return it __modulo__ `` 10^9 + 7 ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "1000", k = 10000
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only possible array is [1000]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "1000", k = 10
<strong>Output:</strong> 0
<strong>Explanation:</strong> There cannot be an array that was printed this way and has all integer &gt;= 1 and &lt;= 10.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "1317", k = 2000
<strong>Output:</strong> 8
<strong>Explanation:</strong> Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "2020", k = 30
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only possible array is [20,20]. [2020] is invalid because 2020 &gt; 30. [2,020] is ivalid because 020 contains leading zeros.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "1234567890", k = 90
<strong>Output:</strong> 34
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= s.length &lt;= 10^5 ``.
*   `` s `` consists of only digits and doesn't contain leading zeros.
*   `` 1 &lt;= k &lt;= 10^9 ``.