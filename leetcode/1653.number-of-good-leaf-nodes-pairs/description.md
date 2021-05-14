Given the `` root `` of a binary tree and an integer `` distance ``. A pair of two different __leaf__ nodes of a binary tree is said to be good if the length of __the shortest path__ between them is less than or equal to `` distance ``.

Return _the number of good leaf node pairs_ in the tree.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/e1.jpg" style="width: 321px; height: 321px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,null,4], distance = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/e2.jpg" style="width: 441px; height: 321px;"/>

<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6,7], distance = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only good pair is [2,5].
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [100], distance = 1
<strong>Output:</strong> 0
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> root = [1,1,1], distance = 2
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the&nbsp;`` tree ``&nbsp;is in the range&nbsp;`` [1, 2^10]. ``
*   Each node's value is between&nbsp;`` [1, 100] ``.
*   `` 1 &lt;= distance &lt;= 10 ``