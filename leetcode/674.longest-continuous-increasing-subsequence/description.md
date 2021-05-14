Given an unsorted array of integers `` nums ``, return _the length of the longest __continuous increasing subsequence__ (i.e. subarray)_. The subsequence must be __strictly__ increasing.

A __continuous increasing subsequence__ is defined by two indices `` l `` and `` r `` (`` l &lt; r ``) such that it is `` [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] `` and for each `` l &lt;= i &lt; r ``, `` nums[i] &lt; nums[i + 1] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,3,5,4,7]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>