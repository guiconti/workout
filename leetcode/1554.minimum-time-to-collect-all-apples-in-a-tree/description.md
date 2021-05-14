Given an undirected tree consisting of `` n `` vertices numbered from `` 0 `` to `` n-1 ``, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. _Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at __vertex 0__ and coming back to this vertex._

The edges of the undirected tree are given in the array `` edges ``, where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> means that exists an edge connecting the vertices <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>. Additionally, there is a boolean array `` hasApple ``, where `` hasApple[i] = true `` means that vertex `` i `` has an apple; otherwise, it does not have any apple.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_1.png" style="width: 300px; height: 212px;"/></strong>

<pre>
<strong>Input:</strong> n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
<strong>Output:</strong> 8 
<strong>Explanation:</strong> The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_2.png" style="width: 300px; height: 212px;"/></strong>

<pre>
<strong>Input:</strong> n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 10^5 ``
*   `` edges.length == n - 1 ``
*   `` edges[i].length == 2 ``
*   <code>0 &lt;= a<sub>i</sub> &lt; b<sub>i</sub> &lt;= n - 1</code>
*   <code>from<sub>i</sub>&nbsp;&lt; to<sub>i</sub></code>
*   `` hasApple.length == n ``