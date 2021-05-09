Given `` n `` non-negative integers representing an elevation map where the width of each bar is `` 1 ``, compute how much water it can trap after raining.

&nbsp;

__Example 1:__

<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;"/>

<pre>
<strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

&nbsp;

__Constraints:__

*   `` n == height.length ``
*   <code>0 &lt;= n &lt;= 3 * 10<sup>4</sup></code>
*   <code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code>