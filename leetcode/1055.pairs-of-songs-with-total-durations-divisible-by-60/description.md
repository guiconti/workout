You are given a list of songs where the i<sup>th</sup> song has a duration of `` time[i] `` seconds.

Return _the number of pairs of songs for which their total duration in seconds is divisible by_ `` 60 ``. Formally, we want the number of indices `` i ``, `` j `` such that `` i &lt; j `` with `` (time[i] + time[j]) % 60 == 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> time = [30,20,150,100,40]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> time = [60,60,60]
<strong>Output:</strong> 3
<strong>Explanation:</strong> All three pairs have a total duration of 120, which is divisible by 60.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= time.length &lt;= 6 * 10<sup>4</sup></code>
*   `` 1 &lt;= time[i] &lt;= 500 ``