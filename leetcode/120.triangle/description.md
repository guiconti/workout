Given a `` triangle `` array, return _the minimum path sum from top to bottom_.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `` i `` on the current row, you may move to either index `` i `` or index `` i + 1 `` on the next row.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The triangle looks like:
   <u>2</u>
  <u>3</u> 4
 6 <u>5</u> 7
4 <u>1</u> 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> triangle = [[-10]]
<strong>Output:</strong> -10
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= triangle.length &lt;= 200 ``
*   `` triangle[0].length == 1 ``
*   `` triangle[i].length == triangle[i - 1].length + 1 ``
*   <code>-10<sup>4</sup> &lt;= triangle[i][j] &lt;= 10<sup>4</sup></code>

&nbsp;
__Follow up:__ Could you&nbsp;do this using only `` O(n) `` extra space, where `` n `` is the total number of rows in the triangle?