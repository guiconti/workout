Given the array of integers `` nums ``, you will choose two different indices `` i `` and `` j `` of that array. _Return the maximum value of_ `` (nums[i]-1)*(nums[j]-1) ``.
&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,4,5,2]
<strong>Output:</strong> 12 
<strong>Explanation:</strong> If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,5,4,5]
<strong>Output:</strong> 16
<strong>Explanation:</strong> Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [3,7]
<strong>Output:</strong> 12
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= nums.length &lt;= 500 ``
*   `` 1 &lt;= nums[i] &lt;= 10^3 ``