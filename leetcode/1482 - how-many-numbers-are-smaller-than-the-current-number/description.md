Given the array `` nums ``, for each `` nums[i] `` find out how many numbers in the array are smaller than it. That is, for each `` nums[i] `` you have to count the number of valid `` j's ``&nbsp;such that&nbsp;`` j != i `` __and__ `` nums[j] &lt; nums[i] ``.

Return the answer in an array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [8,1,2,2,3]
<strong>Output:</strong> [4,0,1,1,3]
<strong>Explanation:</strong> 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [6,5,4,8]
<strong>Output:</strong> [2,1,0,3]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [7,7,7,7]
<strong>Output:</strong> [0,0,0,0]
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= nums.length &lt;= 500 ``
*   `` 0 &lt;= nums[i] &lt;= 100 ``