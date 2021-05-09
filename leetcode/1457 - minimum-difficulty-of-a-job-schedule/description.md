You want to schedule a list of jobs in `` d `` days. Jobs are dependent (i.e To work on the `` i-th `` job, you have to finish all the jobs `` j `` where `` 0 &lt;= j &lt; i ``).

You have to finish __at least__ one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the `` d `` days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers `` jobDifficulty `` and an integer `` d ``. The difficulty of the `` i-th ``&nbsp;job is&nbsp;`` jobDifficulty[i] ``.

Return _the minimum difficulty_ of a job schedule. If you cannot find a schedule for the jobs return __-1__.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/16/untitled.png" style="width: 365px; height: 230px;"/>

<pre>
<strong>Input:</strong> jobDifficulty = [6,5,4,3,2,1], d = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> jobDifficulty = [9,9,9], d = 4
<strong>Output:</strong> -1
<strong>Explanation:</strong> If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> jobDifficulty = [1,1,1], d = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The schedule is one job per day. total difficulty will be 3.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> jobDifficulty = [7,1,7,1,7,1], d = 3
<strong>Output:</strong> 15
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
<strong>Output:</strong> 843
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= jobDifficulty.length &lt;= 300 ``
*   `` 0 &lt;=&nbsp;jobDifficulty[i] &lt;= 1000 ``
*   `` 1 &lt;= d &lt;= 10 ``