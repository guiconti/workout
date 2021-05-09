Return all __non-negative__ integers of length `` n `` such that the absolute difference between every two consecutive digits is `` k ``.

Note that __every__ number in the answer __must not__ have leading zeros. For example, `` 01 `` has one leading zero and is invalid.

You may return the answer in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 3, k = 7
<strong>Output:</strong> [181,292,707,818,929]
<strong>Explanation:</strong> Note that 070 is not a valid number, because it has leading zeroes.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2, k = 1
<strong>Output:</strong> [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 2, k = 0
<strong>Output:</strong> [11,22,33,44,55,66,77,88,99]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 2, k = 2
<strong>Output:</strong> [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 9 ``
*   `` 0 &lt;= k &lt;= 9 ``