You are given an integer array `` jobs ``, where `` jobs[i] `` is the amount of time it takes to complete the <code>i<sup>th</sup></code> job.

There are `` k `` workers that you can assign jobs to. Each job should be assigned to __exactly__ one worker. The __working time__ of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the __maximum working time__ of any worker is __minimized__.

_Return the __minimum__ possible __maximum working time__ of any assignment. _

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> jobs = [3,2,3], k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> By assigning each person one job, the maximum time is 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> jobs = [1,2,4,7,8], k = 2
<strong>Output:</strong> 11
<strong>Explanation:</strong> Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;= jobs.length &lt;= 12 ``
*   <code>1 &lt;= jobs[i] &lt;= 10<sup>7</sup></code>