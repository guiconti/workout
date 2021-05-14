A city's __skyline__ is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return _the __skyline__ formed by these buildings collectively_.

The geometric information of each building is given in the array `` buildings `` where <code>buildings[i] = [left<sub>i</sub>, right<sub>i</sub>, height<sub>i</sub>]</code>:

*   <code>left<sub>i</sub></code> is the x coordinate of the left edge of the <code>i<sup>th</sup></code> building.
*   <code>right<sub>i</sub></code> is the x coordinate of the right edge of the <code>i<sup>th</sup></code> building.
*   <code>height<sub>i</sub></code> is the height of the <code>i<sup>th</sup></code> building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height `` 0 ``.

The __skyline__ should be represented as a list of "key points" __sorted by their x-coordinate__ in the form <code>[[x<sub>1</sub>,y<sub>1</sub>],[x<sub>2</sub>,y<sub>2</sub>],...]</code>. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate `` 0 `` and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

__Note:__ There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `` [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] `` is not acceptable; the three lines of height 5 should be merged into one in the final output as such: `` [...,[2 3],[4 5],[12 7],...] ``

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/merged.jpg" style="width: 800px; height: 331px;"/>

<pre>
<strong>Input:</strong> buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
<strong>Output:</strong> [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
<strong>Explanation:</strong>
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> buildings = [[0,2,3],[2,5,3]]
<strong>Output:</strong> [[0,3],[5,0]]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= buildings.length &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= left<sub>i</sub> &lt; right<sub>i</sub> &lt;= 2<sup>31</sup> - 1</code>
*   <code>1 &lt;= height<sub>i</sub> &lt;= 2<sup>31</sup> - 1</code>
*   `` buildings `` is sorted by <code>left<sub>i</sub></code> in&nbsp;non-decreasing order.