Given an array of integers&nbsp;`` nums ``, you start with an initial __positive__ value _startValue__._

In each iteration, you calculate the step by step sum of _startValue_&nbsp;plus&nbsp;elements in `` nums ``&nbsp;(from left to right).

Return the minimum __positive__ value of&nbsp;_startValue_ such that the step by step sum is never less than 1.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [-3,2,-3,4,2]
<strong>Output:</strong> 5
<strong>Explanation: </strong>If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
<strong>                step by step sum
&nbsp;               startValue = 4 | startValue = 5 | nums
</strong>&nbsp;                 (4 <strong>-3</strong> ) = 1  | (5 <strong>-3</strong> ) = 2    |  -3
&nbsp;                 (1 <strong>+2</strong> ) = 3  | (2 <strong>+2</strong> ) = 4    |   2
&nbsp;                 (3 <strong>-3</strong> ) = 0  | (4 <strong>-3</strong> ) = 1    |  -3
&nbsp;                 (0 <strong>+4</strong> ) = 4  | (1 <strong>+4</strong> ) = 5    |   4
&nbsp;                 (4 <strong>+2</strong> ) = 6  | (5 <strong>+2</strong> ) = 7    |   2
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Minimum start value should be positive. 
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,-2,-3]
<strong>Output:</strong> 5
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 100 ``
*   `` -100 &lt;= nums[i] &lt;= 100 ``