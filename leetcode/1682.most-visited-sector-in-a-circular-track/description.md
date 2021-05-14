Given an integer `` n `` and an integer array `` rounds ``.&nbsp;We&nbsp;have a circular track which consists of `` n `` sectors labeled from `` 1 `` to `` n ``. A marathon will be held on this track, the marathon consists of `` m `` rounds. The <code>i<sup>th</sup></code>&nbsp;round starts at sector `` rounds[i - 1] `` and ends at sector `` rounds[i] ``. For example, round 1 starts at sector `` rounds[0] `` and ends at sector `` rounds[1] ``

Return _an array of the most visited sectors_ sorted in __ascending__ order.

Notice that you&nbsp;circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/14/tmp.jpg" style="width: 433px; height: 341px;"/>

<pre>
<strong>Input:</strong> n = 4, rounds = [1,3,1,2]
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --&gt; 2 --&gt; 3 (end of round 1) --&gt; 4 --&gt; 1 (end of round 2) --&gt; 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2, rounds = [2,1,2,1,2,1,2,1,2]
<strong>Output:</strong> [2]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 7, rounds = [1,3,5,7]
<strong>Output:</strong> [1,2,3,4,5,6,7]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 100 ``
*   `` 1 &lt;= m &lt;= 100 ``
*   `` rounds.length == m + 1 ``
*   `` 1 &lt;= rounds[i] &lt;= n ``
*   `` rounds[i] != rounds[i + 1] `` for `` 0 &lt;= i &lt; m ``