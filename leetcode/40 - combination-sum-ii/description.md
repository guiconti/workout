Given a collection of candidate numbers (`` candidates ``) and a target number (`` target ``), find all unique combinations in `` candidates ``&nbsp;where the candidate numbers sum to `` target ``.

Each number in `` candidates ``&nbsp;may only be used __once__ in the combination.

__Note:__&nbsp;The solution set must not contain duplicate combinations.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;=&nbsp;candidates.length &lt;= 100 ``
*   `` 1 &lt;=&nbsp;candidates[i] &lt;= 50 ``
*   `` 1 &lt;= target &lt;= 30 ``