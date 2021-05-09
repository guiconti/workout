You are given an array of integers&nbsp;`` nums ``, there is a sliding window of size `` k `` which is moving from the very left of the array to the very right. You can only see the `` k `` numbers in the window. Each time the sliding window moves right by one position.

Return _the max sliding window_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,3,-1,-3,5,3,6,7], k = 3
<strong>Output:</strong> [3,3,5,5,6,7]
<strong>Explanation:</strong> 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1], k = 1
<strong>Output:</strong> [1]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,-1], k = 1
<strong>Output:</strong> [1,-1]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [9,11], k = 2
<strong>Output:</strong> [11]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [4,-2], k = 2
<strong>Output:</strong> [4]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   `` 1 &lt;= k &lt;= nums.length ``