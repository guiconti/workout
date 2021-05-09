You have a `` RecentCounter `` class which counts the number of recent requests within a certain time frame.

Implement the `` RecentCounter `` class:

*   `` RecentCounter() `` Initializes the counter with zero recent requests.
*   `` int ping(int t) `` Adds a new request at time `` t ``, where `` t `` represents some time in milliseconds, and returns the number of requests that has happened in the past `` 3000 `` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `` [t - 3000, t] ``.

It is __guaranteed__ that every call to `` ping `` uses a strictly larger value of `` t `` than the previous call.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
<strong>Output</strong>
[null, 1, 2, 3, 3]

<strong>Explanation</strong>
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [<u>1</u>], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [<u>1</u>, <u>100</u>], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [<u>1</u>, <u>100</u>, <u>3001</u>], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, <u>100</u>, <u>3001</u>, <u>3002</u>], range is [2,3002], return 3
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= t &lt;= 10<sup>9</sup></code>
*   Each test case will call `` ping `` with __strictly increasing__ values of `` t ``.
*   At most <code>10<sup>4</sup></code> calls will be made to `` ping ``.