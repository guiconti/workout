Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must&nbsp;write an algorithm with&nbsp;`` O(log n) `` runtime complexity.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

__Example 4:__

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 0
<strong>Output:</strong> 0
</pre>

__Example 5:__

<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   `` nums `` contains __distinct__ values sorted in __ascending__ order.
*   <code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code>