A bus&nbsp;has `` n `` stops numbered from `` 0 `` to `` n - 1 `` that form&nbsp;a circle. We know the distance between all pairs of neighboring stops where `` distance[i] `` is the distance between the stops number&nbsp;`` i `` and `` (i + 1) % n ``.

The bus goes along both directions&nbsp;i.e. clockwise and counterclockwise.

Return the shortest distance between the given&nbsp;`` start ``&nbsp;and `` destination ``&nbsp;stops.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1.jpg" style="width: 388px; height: 240px;"/>

<pre>
<strong>Input:</strong> distance = [1,2,3,4], start = 0, destination = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> Distance between 0 and 1 is 1 or 9, minimum is 1.</pre>

&nbsp;

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1-1.jpg" style="width: 388px; height: 240px;"/>

<pre>
<strong>Input:</strong> distance = [1,2,3,4], start = 0, destination = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> Distance between 0 and 2 is 3 or 7, minimum is 3.
</pre>

&nbsp;

__Example 3:__

<img alt="" src="https://assets.leetcode.com/uploads/2019/09/03/untitled-diagram-1-2.jpg" style="width: 388px; height: 240px;"/>

<pre>
<strong>Input:</strong> distance = [1,2,3,4], start = 0, destination = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> Distance between 0 and 3 is 6 or 4, minimum is 4.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= n&nbsp;&lt;= 10^4 ``
*   `` distance.length == n ``
*   `` 0 &lt;= start, destination &lt; n ``
*   `` 0 &lt;= distance[i] &lt;= 10^4 ``