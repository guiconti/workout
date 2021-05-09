Given 2 integers `` n `` and `` start ``. Your task is return __any__ permutation `` p ``&nbsp;of `` (0,1,2.....,2^n -1)  ``such that :

*   `` p[0] = start ``
*   `` p[i] `` and `` p[i+1] ``&nbsp;differ by only one bit in their binary representation.
*   `` p[0] `` and `` p[2^n -1] ``&nbsp;must also differ by only one bit in their binary representation.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2, start = 3
<strong>Output:</strong> [3,2,0,1]
<strong>Explanation:</strong> The binary representation of the permutation is (11,10,00,01). 
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3, start = 2
<strong>Output:</strong> [2,6,7,5,4,0,1,3]
<strong>Explanation:</strong> The binary representation of the permutation is (010,110,111,101,100,000,001,011).
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 16 ``
*   `` 0 &lt;= start&nbsp;&lt;&nbsp;2 ^ n ``