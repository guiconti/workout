Given a __positive__ integer `` num ``, output its complement number. The complement strategy is to flip the bits of its binary representation.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
</pre>

&nbsp;

__Constraints:__

*   The given integer `` num `` is guaranteed to fit within the range of a 32-bit signed integer.
*   `` num &gt;= 1 ``
*   You could assume no leading zero bit in the integer’s binary representation.
*   This question is the same as 1009:&nbsp;<https://leetcode.com/problems/complement-of-base-10-integer/>