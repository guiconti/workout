You have `` n `` gardens, labeled from `` 1 `` to `` n ``, and an array `` paths `` where <code>paths[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> describes a bidirectional path between garden <code>x<sub>i</sub></code> to garden <code>y<sub>i</sub></code>. In each garden, you want to plant one of 4 types of flowers.

All gardens have __at most 3__ paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return ___any__ such a choice as an array _`` answer ``_, where _`` answer[i] ``_ is the type of flower planted in the _<code>(i+1)<sup>th</sup></code>_ garden. The flower types are denoted _`` 1 ``_, _`` 2 ``_, _`` 3 ``_, or _`` 4 ``_. It is guaranteed an answer exists._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 3, paths = [[1,2],[2,3],[3,1]]
<strong>Output:</strong> [1,2,3]
<strong>Explanation:</strong>
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 4, paths = [[1,2],[3,4]]
<strong>Output:</strong> [1,2,1,2]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
<strong>Output:</strong> [1,2,3,4]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= paths.length &lt;= 2 * 10<sup>4</sup></code>
*   `` paths[i].length == 2 ``
*   <code>1 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= n</code>
*   <code>x<sub>i</sub> != y<sub>i</sub></code>
*   Every garden has __at most 3__ paths coming into or leaving it.