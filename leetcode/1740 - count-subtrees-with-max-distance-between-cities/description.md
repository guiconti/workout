There are `` n `` cities numbered from `` 1 `` to `` n ``. You are given an array `` edges `` of size `` n-1 ``, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> represents a bidirectional edge between cities <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>. There exists a unique path between each pair of cities. In other words, the cities form a __tree__.

A __subtree__ is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each `` d `` from `` 1 `` to `` n-1 ``, find the number of subtrees in which the __maximum distance__ between any two cities in the subtree is equal to `` d ``.

Return _an array of size_ `` n-1 `` _where the _<code>d<sup>th</sup></code>_ __element __(1-indexed)__ is the number of subtrees in which the __maximum distance__ between any two cities is equal to _`` d ``.

__Notice__&nbsp;that&nbsp;the __distance__ between the two cities is the number of edges in the path between them.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/p1.png" style="width: 161px; height: 181px;"/></strong>

<pre>
<strong>Input:</strong> n = 4, edges = [[1,2],[2,3],[2,4]]
<strong>Output:</strong> [3,4,0]
<strong>Explanation:
</strong>The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 2, edges = [[1,2]]
<strong>Output:</strong> [1]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 3, edges = [[1,2],[2,3]]
<strong>Output:</strong> [2,1]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 15 ``
*   `` edges.length == n-1 ``
*   `` edges[i].length == 2 ``
*   <code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code>
*   All pairs <code>(u<sub>i</sub>, v<sub>i</sub>)</code> are distinct.