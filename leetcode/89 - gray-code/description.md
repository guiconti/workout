The gray code is a binary numeral system where two successive values differ in __only one bit__.

Given an integer `` n `` representing the total number of bits in the code, return ___any__ sequence of gray code_.

A gray code sequence must begin with `` 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [0,1,3,2]
<strong>Explanation:</strong>
00 - 0
0<u>1</u> - 1
<u>1</u>1 - 3
1<u>0</u> - 2
[0,2,3,1] is also a valid gray code sequence.
00 - 0
<u>1</u>0 - 2
1<u>1</u> - 3
<u>0</u>1 - 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [0,1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 16 ``