There is an integer array `` nums `` that consists of `` n `` __unique __elements, but you have forgotten it. However, you do remember every pair of adjacent elements in `` nums ``.

You are given a 2D integer array `` adjacentPairs `` of size `` n - 1 `` where each <code>adjacentPairs[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates that the elements <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> are adjacent in `` nums ``.

It is guaranteed that every adjacent pair of elements `` nums[i] `` and `` nums[i+1] `` will exist in `` adjacentPairs ``, either as `` [nums[i], nums[i+1]] `` or `` [nums[i+1], nums[i]] ``. The pairs can appear __in any order__.

Return _the original array _`` nums ``_. If there are multiple solutions, return __any of them___.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> adjacentPairs = [[2,1],[3,4],[3,2]]
<strong>Output:</strong> [1,2,3,4]
<strong>Explanation:</strong> This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> adjacentPairs = [[4,-2],[1,4],[-3,1]]
<strong>Output:</strong> [-2,4,1,-3]
<strong>Explanation:</strong> There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> adjacentPairs = [[100000,-100000]]
<strong>Output:</strong> [100000,-100000]
</pre>

&nbsp;

__Constraints:__

*   `` nums.length == n ``
*   `` adjacentPairs.length == n - 1 ``
*   `` adjacentPairs[i].length == 2 ``
*   <code>2 &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>5</sup> &lt;= nums[i], u<sub>i</sub>, v<sub>i</sub> &lt;= 10<sup>5</sup></code>
*   There exists some `` nums `` that has `` adjacentPairs `` as its pairs.