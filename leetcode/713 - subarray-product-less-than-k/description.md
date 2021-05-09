Your are given an array of positive integers `` nums ``.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than `` k ``.

__Example 1:__  

<pre>
<b>Input:</b> nums = [10, 5, 2, 6], k = 100
<b>Output:</b> 8
<b>Explanation:</b> The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
</pre>

__Note:__<li><code>0 &lt; nums.length &lt;= 50000</code>.</li><li><code>0 &lt; nums[i] &lt; 1000</code>.</li><li><code>0 &lt;= k &lt; 10^6</code>.</li>