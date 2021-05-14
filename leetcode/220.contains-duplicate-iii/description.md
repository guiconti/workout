Given an integer array `` nums `` and two integers `` k `` and `` t ``, return `` true `` if there are __two distinct indices__ `` i `` and `` j `` in the array such that `` abs(nums[i] - nums[j]) &lt;= t `` and `` abs(i - j) &lt;= k ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,2,3,1], k = 3, t = 0
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [1,0,1,1], k = 1, t = 2
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [1,5,9,1,5,9], k = 2, t = 3
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>0 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code>
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>
*   <code>0 &lt;= k &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= t &lt;= 2<sup>31</sup> - 1</code>