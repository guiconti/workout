A magical string `` s `` consists of only `` '1' `` and `` '2' `` and obeys the following rules:

*   The string s is magical because concatenating the number of contiguous occurrences of characters `` '1' `` and `` '2' `` generates the string `` s `` itself.

The first few elements of `` s `` is `` s = "1221121221221121122……" ``. If we group the consecutive `` 1 ``'s and `` 2 ``'s in s, it will be `` "1 22 11 2 1 22 1 22 11 2 11 22 ......" ``&nbsp;and the occurrences of `` 1 ``'s or `` 2 ``'s in each group are `` "1 2 2 1 1 2 1 2 2 1 2 2 ......" ``. You can see that the occurrence sequence is `` s `` itself.

Given an integer `` n ``, return the number of `` 1 ``'s in the first `` n `` number in the magical string `` s ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first 6 elements of magical string s is "12211" and it contains three 1's, so return 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>