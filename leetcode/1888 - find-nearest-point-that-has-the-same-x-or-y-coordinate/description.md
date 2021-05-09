You are given two integers, `` x `` and `` y ``, which represent your current location on a Cartesian grid: `` (x, y) ``. You are also given an array `` points `` where each <code>points[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> represents that a point exists at <code>(a<sub>i</sub>, b<sub>i</sub>)</code>. A point is __valid__ if it shares the same x-coordinate or the same y-coordinate as your location.

Return _the index __(0-indexed)__ of the __valid__ point with the smallest __Manhattan distance__ from your current location_. If there are multiple, return _the valid point with the __smallest__ index_. If there are no valid points, return `` -1 ``.

The __Manhattan distance__ between two points <code>(x<sub>1</sub>, y<sub>1</sub>)</code> and <code>(x<sub>2</sub>, y<sub>2</sub>)</code> is <code>abs(x<sub>1</sub> - x<sub>2</sub>) + abs(y<sub>1</sub> - y<sub>2</sub>)</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> x = 3, y = 4, points = [[3,4]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The answer is allowed to be on the same location as your current location.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> x = 3, y = 4, points = [[2,3]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There are no valid points.</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= points.length &lt;= 10<sup>4</sup></code>
*   `` points[i].length == 2 ``
*   <code>1 &lt;= x, y, a<sub>i</sub>, b<sub>i</sub> &lt;= 10<sup>4</sup></code>