You are given an integer array `` nums `` consisting of `` n `` elements, and an integer `` k ``.

Find a contiguous subarray whose __length is equal to__ `` k `` that has the maximum average value and return _this value_. Any answer with a calculation error less than <code>10<sup>-5</sup></code> will be accepted.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,12,-5,-6,50,3], k = 4
<strong>Output:</strong> 12.75000
<strong>Explanation:</strong> Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [5], k = 1
<strong>Output:</strong> 5.00000
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= k &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>