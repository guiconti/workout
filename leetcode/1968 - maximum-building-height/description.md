You want to build `` n `` new buildings in a city. The new buildings will be built in a line and are labeled from `` 1 `` to `` n ``.

However, there are city restrictions on the heights of the new buildings:

*   The height of each building must be a non-negative integer.
*   The height of the first building __must__ be `` 0 ``.
*   The height difference between any two adjacent buildings __cannot exceed__ `` 1 ``.

Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array `` restrictions `` where <code>restrictions[i] = [id<sub>i</sub>, maxHeight<sub>i</sub>]</code> indicates that building <code>id<sub>i</sub></code> must have a height __less than or equal to__ <code>maxHeight<sub>i</sub></code>.

It is guaranteed that each building will appear __at most once__ in `` restrictions ``, and building `` 1 `` will __not__ be in `` restrictions ``.

Return _the __maximum possible height__ of the __tallest__ building_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex1-1.png" style="width: 400px; height: 253px;"/>

<pre>
<strong>Input:</strong> n = 5, restrictions = [[2,1],[4,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex2.png" style="width: 500px; height: 269px;"/>

<pre>
<strong>Input:</strong> n = 6, restrictions = []
<strong>Output:</strong> 5
<strong>Explanation:</strong> The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.
</pre>

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex3.png" style="width: 500px; height: 187px;"/>

<pre>
<strong>Input:</strong> n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= n &lt;= 10<sup>9</sup></code>
*   <code>0 &lt;= restrictions.length &lt;= min(n - 1, 10<sup>5</sup>)</code>
*   <code>2 &lt;= id<sub>i</sub> &lt;= n</code>
*   <code>id<sub>i</sub></code>&nbsp;is __unique__.
*   <code>0 &lt;= maxHeight<sub>i</sub> &lt;= 10<sup>9</sup></code>