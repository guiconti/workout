You are given an undirected graph represented by an integer `` n ``, which is the number of nodes, and `` edges ``, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> which indicates that there is an undirected edge between <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>. You are also given an integer array `` queries ``.

The answer to the <code>j<sup>th</sup></code> query is the number of pairs of nodes `` (a, b) `` that satisfy the following conditions:

*   `` a &lt; b ``
*   `` cnt `` is __strictly greater__ than `` queries[j] ``, where `` cnt `` is the number of edges incident to `` a `` __or__ `` b ``.

Return an array `` answers `` such that `` answers.length == queries.length `` and `` answers[j] `` is the answer of the <code>j<sup>th</sup></code> query.

Note that there can be __repeated edges__.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/11/screenshot-from-2021-02-11-23-07-35.png" style="width: 310px; height: 278px;"/>

<pre>
<strong>Input:</strong> n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
<strong>Output:</strong> [6,5]
<strong>Explanation:</strong> The number of edges incident to at least one of each pair is shown above.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
<strong>Output:</strong> [10,10,9,8,6]
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= n &lt;= 2 * 10<sup>4</sup></code>
*   <code>1 &lt;= edges.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code>
*   <code>u<sub>i </sub>!= v<sub>i</sub></code>
*   `` 1 &lt;= queries.length &lt;= 20 ``
*   `` 0 &lt;= queries[j] &lt; edges.length ``