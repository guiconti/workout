There are a total of `` numCourses `` courses you have to take, labeled from `` 0 `` to `` numCourses - 1 ``. You are given an array `` prerequisites `` where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you __must__ take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.

*   For example, the pair `` [0, 1] ``, indicates that to take course `` 0 `` you have to first take course `` 1 ``.

Return `` true `` if you can finish all courses. Otherwise, return `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= numCourses &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= prerequisites.length &lt;= 5000 ``
*   `` prerequisites[i].length == 2 ``
*   <code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code>
*   All the pairs prerequisites\[i\] are __unique__.