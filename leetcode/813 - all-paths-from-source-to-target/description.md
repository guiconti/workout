Given a directed&nbsp;acyclic graph (__DAG__) of `` n `` nodes labeled from 0 to n - 1,&nbsp;find all possible paths from node `` 0 `` to node `` n - 1 ``, and return them in any order.

The graph is given as follows:&nbsp;`` graph[i] `` is a list of all nodes you can visit from node `` i ``&nbsp;(i.e., there is a directed edge from node `` i `` to node `` graph[i][j] ``).

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg" style="width: 242px; height: 242px;"/>

<pre>
<strong>Input:</strong> graph = [[1,2],[3],[3],[]]
<strong>Output:</strong> [[0,1,3],[0,2,3]]
<strong>Explanation:</strong> There are two paths: 0 -&gt; 1 -&gt; 3 and 0 -&gt; 2 -&gt; 3.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg" style="width: 423px; height: 301px;"/>

<pre>
<strong>Input:</strong> graph = [[4,3,1],[3,2,4],[3],[4],[]]
<strong>Output:</strong> [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> graph = [[1],[]]
<strong>Output:</strong> [[0,1]]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> graph = [[1,2,3],[2],[3],[]]
<strong>Output:</strong> [[0,1,2,3],[0,2,3],[0,3]]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> graph = [[1,3],[2],[3],[]]
<strong>Output:</strong> [[0,1,2,3],[0,3]]
</pre>

&nbsp;

__Constraints:__

*   `` n == graph.length ``
*   `` 2 &lt;= n &lt;= 15 ``
*   `` 0 &lt;= graph[i][j] &lt; n ``
*   `` graph[i][j] != i `` (i.e., there will be no self-loops).
*   The input graph is __guaranteed__ to be a __DAG__.