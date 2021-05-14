Given two integer arrays `` startTime `` and `` endTime `` and given an integer `` queryTime ``.

The `` ith `` student started doing their homework at the time `` startTime[i] `` and finished it at time `` endTime[i] ``.

Return _the number of students_ doing their homework at time `` queryTime ``. More formally, return the number of students where `` queryTime ``&nbsp;lays in the interval `` [startTime[i], endTime[i]] `` inclusive.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> startTime = [4], endTime = [4], queryTime = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only student was doing their homework at the queryTime.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> startTime = [4], endTime = [4], queryTime = 5
<strong>Output:</strong> 0
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
<strong>Output:</strong> 0
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   `` startTime.length == endTime.length ``
*   `` 1 &lt;= startTime.length &lt;= 100 ``
*   `` 1 &lt;= startTime[i] &lt;= endTime[i] &lt;= 1000 ``
*   `` 1 &lt;=&nbsp;queryTime &lt;= 1000 ``