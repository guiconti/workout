We have jobs: `` difficulty[i] ``&nbsp;is the difficulty of the&nbsp;`` i ``th job, and&nbsp;`` profit[i] ``&nbsp;is the profit of the&nbsp;`` i ``th job.&nbsp;

Now we have some workers.&nbsp;`` worker[i] ``&nbsp;is the ability of the&nbsp;`` i ``th worker, which means that this worker can only complete a job with difficulty at most&nbsp;`` worker[i] ``.&nbsp;

Every worker can be assigned at most one job, but one job&nbsp;can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.&nbsp; If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

__Example 1:__

<pre>
<strong>Input: </strong>difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
<strong>Output: </strong>100 
<strong>Explanation: W</strong>orkers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.</pre>

__Notes:__

*   `` 1 &lt;= difficulty.length = profit.length &lt;= 10000 ``
*   `` 1 &lt;= worker.length &lt;= 10000 ``
*   `` difficulty[i], profit[i], worker[i] ``&nbsp; are in range&nbsp;`` [1, 10^5] ``