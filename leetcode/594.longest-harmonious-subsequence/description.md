We define a harmonious array as an array where the difference between its maximum value and its minimum value is __exactly__ `` 1 ``.

Given an integer array `` nums ``, return _the length of its longest harmonious subsequence among all its possible subsequences_.

A __subsequence__ of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,3,2,2,5,2,3,7]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest harmonious subsequence is [3,2,2,2,3].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,1,1,1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code>
*   <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>