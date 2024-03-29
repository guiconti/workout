There are a total of `` numCourses `` courses you have to take, labeled from `` 0 `` to `` numCourses - 1 ``. You are given an array `` prerequisites `` where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you __must__ take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.

*   For example, the pair `` [0, 1] ``, indicates that to take course `` 0 `` you have to first take course `` 1 ``.

Return _the ordering of courses you should take to finish all courses_. If there are many valid answers, return __any__ of them. If it is impossible to finish all courses, return __an empty array__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
<strong>Output:</strong> [0,2,1,3]
<strong>Explanation:</strong> There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> numCourses = 1, prerequisites = []
<strong>Output:</strong> [0]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= numCourses &lt;= 2000 ``
*   `` 0 &lt;= prerequisites.length &lt;= numCourses * (numCourses - 1) ``
*   `` prerequisites[i].length == 2 ``
*   <code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are __distinct__.