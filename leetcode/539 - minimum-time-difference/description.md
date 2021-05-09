Given a list of 24-hour clock time points in __"HH:MM"__ format, return _the minimum __minutes__ difference between any two time-points in the list_.
&nbsp;

__Example 1:__

<pre><strong>Input:</strong> timePoints = ["23:59","00:00"]
<strong>Output:</strong> 1
</pre>

__Example 2:__

<pre><strong>Input:</strong> timePoints = ["00:00","23:59","00:00"]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= timePoints &lt;= 2 * 10<sup>4</sup></code>
*   `` timePoints[i] `` is in the format __"HH:MM"__.