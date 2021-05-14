Given a positive integer `` n ``, find and return _the __longest distance__ between any two __adjacent__ _`` 1 ``_'s in the binary representation of _`` n ``_. If there are no two adjacent _`` 1 ``_'s, return _`` 0 ``_._

Two `` 1 ``'s are __adjacent__ if there are only `` 0 ``'s separating them (possibly no `` 0 ``'s). The __distance__ between two `` 1 ``'s is the absolute difference between their bit positions. For example, the two `` 1 ``'s in `` "1001" `` have a distance of 3.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 22
<strong>Output:</strong> 2
<strong>Explanation:</strong> 22 in binary is "10110".
The first adjacent pair of 1's is "<u>1</u>0<u>1</u>10" with a distance of 2.
The second adjacent pair of 1's is "10<u>11</u>0" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "<u>1</u>01<u>1</u>0" is not a valid pair since there is a 1 separating the two 1's underlined.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> 5 in binary is "101".
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 1
<strong>Explanation:</strong> 6 in binary is "110".
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 8
<strong>Output:</strong> 0
<strong>Explanation:</strong> 8 in binary is "1000".
There aren't any adjacent pairs of 1's in the binary representation of 8, so we return 0.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>9</sup></code>