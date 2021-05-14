Given an integer&nbsp;`` n ``.&nbsp;Each number from `` 1 `` to `` n `` is grouped according to the sum of its digits.&nbsp;

Return&nbsp;how many groups have the largest size.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 13
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 groups [1], [2] of size 1.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 15
<strong>Output:</strong> 6
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 24
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^4 ``