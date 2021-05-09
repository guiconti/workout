Given an array of integers `` nums `` and a positive integer `` k ``, find whether it's possible to divide this array into sets of `` k `` consecutive numbers  
Return `` True `` if it is possible.__ __Otherwise, return `` False ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,3,4,4,5,6], k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> Array can be divided into [1,2,3,4] and [3,4,5,6].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [3,3,2,2,1,1], k = 3
<strong>Output:</strong> true
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4], k = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> Each array should be divided in subarrays of size 3.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code>

&nbsp;
__Note:__ This question is the same as&nbsp;846:&nbsp;<a href="https://leetcode.com/problems/hand-of-straights/" target="_blank">https://leetcode.com/problems/hand-of-straights/</a>