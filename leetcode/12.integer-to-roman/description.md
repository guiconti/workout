Roman numerals are represented by seven different symbols:&nbsp;`` I ``, `` V ``, `` X ``, `` L ``, `` C ``, `` D `` and `` M ``.

<pre>
<strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

For example,&nbsp;`` 2 `` is written as `` II ``&nbsp;in Roman numeral, just two one's added together. `` 12 `` is written as&nbsp;`` XII ``, which is simply `` X + II ``. The number `` 27 `` is written as `` XXVII ``, which is `` XX + V + II ``.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `` IIII ``. Instead, the number four is written as `` IV ``. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `` IX ``. There are six instances where subtraction is used:

*   `` I `` can be placed before `` V `` (5) and `` X `` (10) to make 4 and 9.&nbsp;
*   `` X `` can be placed before `` L `` (50) and `` C `` (100) to make 40 and 90.&nbsp;
*   `` C `` can be placed before `` D `` (500) and `` M `` (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = 3
<strong>Output:</strong> "III"
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = 4
<strong>Output:</strong> "IV"
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = 9
<strong>Output:</strong> "IX"
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> num = 58
<strong>Output:</strong> "LVIII"
<strong>Explanation:</strong> L = 50, V = 5, III = 3.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> num = 1994
<strong>Output:</strong> "MCMXCIV"
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= num &lt;= 3999 ``