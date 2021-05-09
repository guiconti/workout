Given `` n `` points on a 1-D plane, where the <code>i<sup>th</sup></code> point (from `` 0 `` to `` n-1 ``) is at `` x = i ``, find the number of ways we can draw __exactly__ `` k `` __non-overlapping__ line segments such that each segment covers two or more points. The endpoints of each segment must have __integral coordinates__. The `` k `` line segments __do not__ have to cover all `` n `` points, and they are __allowed__ to share endpoints.

Return _the number of ways we can draw _`` k ``_ non-overlapping line segments__._&nbsp;Since this number can be huge, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/07/ex1.png" style="width: 179px; height: 222px;"/>

<pre>
<strong>Input:</strong> n = 4, k = 2
<strong>Output:</strong> 5
<strong>Explanation: 
</strong>The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> 3
<strong>Explanation: </strong>The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> n = 30, k = 7
<strong>Output:</strong> 796297179
<strong>Explanation: </strong>The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 10<sup>9</sup> + 7 gives us 796297179.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> n = 5, k = 3
<strong>Output:</strong> 7
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> n = 3, k = 2
<strong>Output:</strong> 1</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= n &lt;= 1000 ``
*   `` 1 &lt;= k &lt;= n-1 ``