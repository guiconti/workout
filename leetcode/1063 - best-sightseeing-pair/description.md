You are given an integer array `` values `` where values\[i\] represents the value of the <code>i<sup>th</sup></code> sightseeing spot. Two sightseeing spots `` i `` and `` j `` have a __distance__ `` j - i `` between them.

The score of a pair (`` i &lt; j ``) of sightseeing spots is `` values[i] + values[j] + i - j ``: the sum of the values of the sightseeing spots, minus the distance between them.

Return _the maximum score of a pair of sightseeing spots_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> values = [8,1,5,2,6]
<strong>Output:</strong> 11
<strong>Explanation:</strong> i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> values = [1,2]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= values.length &lt;= 5 * 10<sup>4</sup></code>
*   `` 1 &lt;= values[i] &lt;= 1000 ``