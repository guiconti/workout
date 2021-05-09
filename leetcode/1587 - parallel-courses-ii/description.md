Given the integer `` n `` representing the number of courses at some university labeled from `` 1 `` to `` n ``, and the array `` dependencies `` where <code>dependencies[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a prerequisite relationship, that is, the course <code>x<sub>i</sub></code> must be taken before the course <code>y<sub>i</sub></code>. Also, you are given the integer `` k ``.

In one semester you can take __at most__ `` k `` courses as long as you have taken all the prerequisites for the courses you are taking.

_Return the minimum number of semesters to take all courses_. It is guaranteed that you can take all courses in some way.

&nbsp;

__Example 1:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/05/22/leetcode_parallel_courses_1.png" style="width: 300px; height: 164px;"/></strong>

<pre>
<strong>Input:</strong> n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
<strong>Output:</strong> 3 
<strong>Explanation:</strong> The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
</pre>

__Example 2:__

<strong><img alt="" src="https://assets.leetcode.com/uploads/2020/05/22/leetcode_parallel_courses_2.png" style="width: 300px; height: 234px;"/></strong>

<pre>
<strong>Input:</strong> n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
<strong>Output:</strong> 4 
<strong>Explanation:</strong> The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 11, dependencies = [], k = 2
<strong>Output:</strong> 6
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n &lt;= 15 ``
*   `` 1 &lt;= k &lt;= n ``
*   `` 0 &lt;= dependencies.length &lt;= n * (n-1) / 2 ``
*   `` dependencies[i].length == 2 ``
*   <code>1 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= n</code>
*   <code>x<sub>i</sub> != y<sub>i</sub></code>
*   All prerequisite relationships are distinct, that is, `` dependencies[i] != dependencies[j] ``.
*   The given graph is a directed acyclic graph.