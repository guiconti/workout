Given an array `` nums ``, you are allowed to choose one element of `` nums `` and change it by any&nbsp;value in one move.

Return the minimum difference between the largest and smallest value of `` nums ``&nbsp;after perfoming at most 3 moves.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [5,3,2,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Change the array [5,3,2,4] to [<strong>2</strong>,<strong>2</strong>,2,<strong>2</strong>].
The difference between the maximum and minimum is 2-2 = 0.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,5,0,10,14]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Change the array [1,5,0,10,14] to [1,<strong>1</strong>,0,<strong>1</strong>,<strong>1</strong>]. 
The difference between the maximum and minimum is 1-0 = 1.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [6,6,0,1,1,4,6]
<strong>Output:</strong> 2
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [1,5,6,14,15]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10^5 ``
*   `` -10^9 &lt;= nums[i] &lt;= 10^9 ``