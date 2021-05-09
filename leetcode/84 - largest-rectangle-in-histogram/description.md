Given an array of integers `` heights `` representing the histogram's bar height where the width of each bar is `` 1 ``, return _the area of the largest rectangle in the histogram_.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" style="width: 522px; height: 242px;"/>

<pre>
<strong>Input:</strong> heights = [2,1,5,6,2,3]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" style="width: 202px; height: 362px;"/>

<pre>
<strong>Input:</strong> heights = [2,4]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= heights.length &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= heights[i] &lt;= 10<sup>4</sup></code>