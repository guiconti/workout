You are given an integer `` num ``. You will apply the following steps exactly __two__ times:

*   Pick a digit `` x (0&nbsp;&lt;= x &lt;= 9) ``.
*   Pick another digit `` y (0&nbsp;&lt;= y &lt;= 9) ``. The digit `` y `` can be equal to `` x ``.
*   Replace all the occurrences of `` x `` in the decimal representation of `` num `` by `` y ``.
*   The new integer __cannot__ have any leading zeros, also the new integer __cannot__ be 0.

Let `` a ``&nbsp;and `` b ``&nbsp;be the results of applying the operations to `` num `` the first and second times, respectively.

Return _the max difference_ between `` a `` and `` b ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = 555
<strong>Output:</strong> 888
<strong>Explanation:</strong> The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = 9
<strong>Output:</strong> 8
<strong>Explanation:</strong> The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = 123456
<strong>Output:</strong> 820000
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> num = 10000
<strong>Output:</strong> 80000
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> num = 9288
<strong>Output:</strong> 8700
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= num &lt;= 10^8 ``