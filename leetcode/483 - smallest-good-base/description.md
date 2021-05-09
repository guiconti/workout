Given an integer `` n `` represented as a string, return _the smallest __good base__ of_ `` n ``.

We call `` k &gt;= 2 `` a __good base__ of `` n ``, if all digits of `` n `` base `` k `` are `` 1 ``'s.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = "13"
<strong>Output:</strong> "3"
<strong>Explanation:</strong> 13 base 3 is 111.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = "4681"
<strong>Output:</strong> "8"
<strong>Explanation:</strong> 4681 base 8 is 11111.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = "1000000000000000000"
<strong>Output:</strong> "999999999999999999"
<strong>Explanation:</strong> 1000000000000000000 base 999999999999999999 is 11.
</pre>

&nbsp;

__Constraints:__

*   `` n `` is an integer in the range <code>[3, 10<sup>18</sup>]</code>.
*   `` n `` does not contain any leading zeros.