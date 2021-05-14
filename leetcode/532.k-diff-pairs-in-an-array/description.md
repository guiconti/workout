Given an array of integers `` nums `` and an integer `` k ``, return _the number of __unique__ k-diff pairs in the array_.

A __k-diff__ pair is an integer pair `` (nums[i], nums[j]) ``, where the following are true:

*   `` 0 &lt;= i &lt; j &lt; nums.length ``
*   `` |nums[i] - nums[j]| == k ``

__Notice__ that `` |val| `` denotes the absolute value of `` val ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,1,4,1,5], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of <strong>unique</strong> pairs.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5], k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,3,1,5,4], k = 0
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is one 0-diff pair in the array, (1, 1).
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [1,2,4,4,3,3,0,9,2,3], k = 3
<strong>Output:</strong> 2
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [-1,-2,-3], k = 1
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></code>
*   <code>0 &lt;= k &lt;= 10<sup>7</sup></code>