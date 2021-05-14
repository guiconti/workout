There are a total of `` numCourses `` courses you have to take, labeled from `` 0 `` to `` numCourses - 1 ``. You are given an array `` prerequisites `` where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you __must__ take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.

*   For example, the pair `` [0, 1] ``, indicates that to take course `` 0 `` you have to first take course `` 1 ``.

You are also given an array `` queries `` where <code>queries[j] = [u<sub>j</sub>, v<sub>j</sub>]</code>. For the <code>j<sup>th</sup></code> query, you should answer whether the course <code>u<sub>j</sub></code> is a prerequisite of the course <code>v<sub>j</sub></code> or not. Note that if course `` a `` is a prerequisite of course `` b `` and course `` b `` is a prerequisite of course `` c ``, then, course `` a `` is a prerequisite of course `` c ``.

Return _a boolean array _`` answer ``_, where _`` answer[j] ``_ is the answer of the _<code>j<sup>th</sup></code>_ query._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg" style="width: 222px; height: 62px;"/>

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
<strong>Output:</strong> [false,true]
<strong>Explanation:</strong> course 0 is not a prerequisite of course 1 but the opposite is true.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
<strong>Output:</strong> [false,false]
<strong>Explanation:</strong> There are no prerequisites and each course is independent.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/courses4-3-graph.jpg" style="width: 222px; height: 222px;"/>

<pre>
<strong>Input:</strong> numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
<strong>Output:</strong> [true,true]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= numCourses &lt;= 100 ``
*   `` 0 &lt;= prerequisite.length &lt;= (numCourses * (numCourses - 1) / 2) ``
*   <code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are __unique__.
*   The prerequisites graph has no cycles.
*   <code>1 &lt;= queries.length &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; n</code>
*   <code>u<sub>i</sub> != v<sub>i</sub></code>