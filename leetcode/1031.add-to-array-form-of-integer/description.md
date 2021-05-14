The __array-form__ of an integer `` num `` is an array representing its digits in left to right order.

*   For example, for `` num = 1321 ``, the array form is `` [1,3,2,1] ``.

Given `` num ``, the __array-form__ of an integer, and an integer `` k ``, return _the __array-form__ of the integer_ `` num + k ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = [1,2,0,0], k = 34
<strong>Output:</strong> [1,2,3,4]
<strong>Explanation:</strong> 1200 + 34 = 1234
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = [2,7,4], k = 181
<strong>Output:</strong> [4,5,5]
<strong>Explanation:</strong> 274 + 181 = 455
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = [2,1,5], k = 806
<strong>Output:</strong> [1,0,2,1]
<strong>Explanation:</strong> 215 + 806 = 1021
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> num = [9,9,9,9,9,9,9,9,9,9], k = 1
<strong>Output:</strong> [1,0,0,0,0,0,0,0,0,0,0]
<strong>Explanation:</strong> 9999999999 + 1 = 10000000000
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= num.length &lt;= 10<sup>4</sup></code>
*   `` 0 &lt;= num[i] &lt;= 9 ``
*   `` num ``&nbsp;does not contain any leading zeros except for the zero itself.
*   <code>1 &lt;= k &lt;= 10<sup>4</sup></code>