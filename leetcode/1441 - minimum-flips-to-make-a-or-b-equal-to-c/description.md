Given 3 positives numbers `` a ``, `` b `` and `` c ``. Return the minimum flips required in some bits of `` a `` and `` b `` to make (&nbsp;`` a `` OR `` b `` == `` c ``&nbsp;). (bitwise OR operation).  
Flip operation&nbsp;consists of change&nbsp;__any__&nbsp;single bit 1 to 0 or change the bit 0 to 1&nbsp;in their binary representation.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/06/sample_3_1676.png" style="width: 260px; height: 87px;"/>

<strong>Input:</strong> a = 2, b = 6, c = 5
    <strong>Output:</strong> 3
    <strong>Explanation: </strong>After flips a = 1 , b = 4 , c = 5 such that (a OR <code>b</code> == <code>c</code>)

__Example 2:__

<pre>
<strong>Input:</strong> a = 4, b = 2, c = 7
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> a = 1, b = 2, c = 3
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= a &lt;= 10^9 ``
*   `` 1 &lt;= b&nbsp;&lt;= 10^9 ``
*   `` 1 &lt;= c&nbsp;&lt;= 10^9 ``