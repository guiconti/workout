An undirected graph of `` n `` nodes is defined by `` edgeList ``, where <code>edgeList[i] = [u<sub>i</sub>, v<sub>i</sub>, dis<sub>i</sub>]</code> denotes an edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> with distance <code>dis<sub>i</sub></code>. Note that there may be __multiple__ edges between two nodes.

Given an array `` queries ``, where <code>queries[j] = [p<sub>j</sub>, q<sub>j</sub>, limit<sub>j</sub>]</code>, your task is to determine for each `` queries[j] `` whether there is a path between <code>p<sub>j</sub></code> and <code>q<sub>j</sub></code><sub> </sub>such that each edge on the path has a distance __strictly less than__ <code>limit<sub>j</sub></code> .

Return _a __boolean array__ _`` answer ``_, where _`` answer.length == queries.length `` _and the _<code>j<sup>th</sup></code> _value of _`` answer `` _is _`` true ``_ if there is a path for _`` queries[j] ``_ is _`` true ``_, and _`` false ``_ otherwise_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/08/h.png" style="width: 267px; height: 262px;"/>

<pre>
<strong>Input:</strong> n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
<strong>Output:</strong> [false,true]
<strong>Explanation:</strong> The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -&gt; 1 -&gt; 2) of two edges with distances less than 5, thus we return true for this query.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/08/q.png" style="width: 390px; height: 358px;"/>

<pre>
<strong>Input:</strong> n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
<strong>Output:</strong> [true,false]
<strong>Exaplanation:</strong> The above figure shows the given graph.
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= edgeList.length, queries.length &lt;= 10<sup>5</sup></code>
*   `` edgeList[i].length == 3 ``
*   `` queries[j].length == 3 ``
*   <code>0 &lt;= u<sub>i</sub>, v<sub>i</sub>, p<sub>j</sub>, q<sub>j</sub> &lt;= n - 1</code>
*   <code>u<sub>i</sub> != v<sub>i</sub></code>
*   <code>p<sub>j</sub> != q<sub>j</sub></code>
*   <code>1 &lt;= dis<sub>i</sub>, limit<sub>j</sub> &lt;= 10<sup>9</sup></code>
*   There may be __multiple__ edges between two nodes.