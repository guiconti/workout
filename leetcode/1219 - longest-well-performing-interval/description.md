We are given `` hours ``, a list of the number of hours&nbsp;worked per day for a given employee.

A day is considered to be a _tiring day_ if and only if the number of hours worked is (strictly) greater than `` 8 ``.

A _well-performing interval_ is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> hours = [9,9,6,0,6,6,9]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The longest well-performing interval is [9,9,6].
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= hours.length &lt;= 10000 ``
*   `` 0 &lt;= hours[i] &lt;= 16 ``