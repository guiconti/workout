Given an integer array `` nums `` and an integer `` k ``, return `` true `` if there are two __distinct indices__ `` i `` and `` j `` in the array such that `` nums[i] == nums[j] `` and `` abs(i - j) &lt;= k ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,1], k = 3
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,0,1,1], k = 1
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3,1,2,3], k = 2
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
*   <code>0 &lt;= k &lt;= 10<sup>5</sup></code>