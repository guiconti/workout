We have `` n `` cities labeled from `` 1 `` to `` n ``. Two different cities with labels `` x `` and `` y `` are directly connected by a bidirectional road if and only if `` x `` and `` y `` share a common divisor __strictly greater__ than some `` threshold ``. More formally, cities with labels `` x `` and `` y `` have a road between them if there exists an integer `` z `` such that all of the following are true:

*   `` x % z == 0 ``,
*   `` y % z == 0 ``, and
*   `` z &gt; threshold ``.

Given the two integers, `` n `` and `` threshold ``, and an array of `` queries ``, you must determine for each <code>queries[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> if cities <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> are connected directly or indirectly.&nbsp;(i.e. there is some path between them).

Return _an array _`` answer ``_, where _`` answer.length == queries.length ``_ and _`` answer[i] ``_ is _`` true ``_ if for the _<code>i<sup>th</sup></code>_ query, there is a path between _<code>a<sub>i</sub></code>_ and _<code>b<sub>i</sub></code>_, or _`` answer[i] ``_ is _`` false ``_ if there is no path._

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/09/ex1.jpg" style="width: 382px; height: 181px;"/>

<pre>
<strong>Input:</strong> n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
<strong>Output:</strong> [false,false,true]
<strong>Explanation:</strong> The divisors for each number:
1:   1
2:   1, 2
3:   1, <u>3</u>
4:   1, 2, <u>4</u>
5:   1, <u>5</u>
6:   1, 2, <u>3</u>, <u>6</u>
Using the underlined divisors above the threshold, only cities 3 and 6 share a common divisor, so they are the
only ones directly connected. The result of each query:
[1,4]   1 is not connected to 4
[2,5]   2 is not connected to 5
[3,6]   3 is connected to 6 through path 3--6
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/10/tmp.jpg" style="width: 532px; height: 302px;"/>

<pre>
<strong>Input:</strong> n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
<strong>Output:</strong> [true,true,true,true,true]
<strong>Explanation:</strong> The divisors for each number are the same as the previous example. However, since the threshold is 0,
all divisors can be used. Since all numbers share 1 as a divisor, all cities are connected.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/17/ex3.jpg" style="width: 282px; height: 282px;"/>

<pre>
<strong>Input:</strong> n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
<strong>Output:</strong> [false,false,false,false,false]
<strong>Explanation:</strong> Only cities 2 and 4 share a common divisor 2 which is strictly greater than the threshold 1, so they are the only ones directly connected.
Please notice that there can be multiple queries for the same pair of nodes [x, y], and that the query [x, y] is equivalent to the query [y, x].
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= n &lt;= 10<sup>4</sup></code>
*   `` 0 &lt;= threshold &lt;= n ``
*   <code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code>
*   `` queries[i].length == 2 ``
*   <code>1 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= cities</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>