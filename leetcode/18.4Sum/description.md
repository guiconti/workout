Given an array `` nums `` of `` n `` integers, return _an array of all the __unique__ quadruplets_ `` [nums[a], nums[b], nums[c], nums[d]] `` such that:

*   `` 0 &lt;= a, b, c, d&nbsp;&lt; n ``
*   `` a ``, `` b ``, `` c ``, and `` d `` are __distinct__.
*   `` nums[a] + nums[b] + nums[c] + nums[d] == target ``

You may return the answer in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,0,-1,0,-2,2], target = 0
<strong>Output:</strong> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2], target = 8
<strong>Output:</strong> [[2,2,2,2]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 200 ``
*   <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
*   <code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code>