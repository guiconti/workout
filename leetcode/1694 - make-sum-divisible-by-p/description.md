Given an array of positive integers `` nums ``, remove the __smallest__ subarray (possibly __empty__) such that the __sum__ of the remaining elements is divisible by `` p ``. It is __not__ allowed to remove the whole array.

Return _the length of the smallest subarray that you need to remove, or _`` -1 ``_ if it's impossible_.

A __subarray__ is defined as a contiguous block of elements in the array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,1,4,2], p = 6
<strong>Output:</strong> 1
<strong>Explanation:</strong> The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [6,3,5,2], p = 9
<strong>Output:</strong> 2
<strong>Explanation:</strong> We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3], p = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [1,2,3], p = 7
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no way to remove a subarray in order to get a sum divisible by 7.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [1000000000,1000000000,1000000000], p = 3
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code>
*   <code>1 &lt;= p &lt;= 10<sup>9</sup></code>