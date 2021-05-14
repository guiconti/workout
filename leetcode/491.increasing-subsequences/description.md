Given an integer array `` nums ``, return all the different possible increasing subsequences of the given array with __at least two elements__. You may return the answer in __any order__.

The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [4,6,7,7]
<strong>Output:</strong> [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [4,4,3,2,1]
<strong>Output:</strong> [[4,4]]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 15 ``
*   `` -100 &lt;= nums[i] &lt;= 100 ``