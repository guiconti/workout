Given an array of integers&nbsp;`` nums ``.

A pair&nbsp;`` (i,j) ``&nbsp;is called _good_ if&nbsp;`` nums[i] `` == `` nums[j] `` and `` i `` &lt; `` j ``.

Return the number of _good_ pairs.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,1,1,3]
<strong>Output:</strong> 4
<strong>Explanation: </strong>There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,1,1,1]
<strong>Output:</strong> 6
<strong>Explanation: </strong>Each pair in the array are <em>good</em>.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 100 ``
*   `` 1 &lt;= nums[i] &lt;= 100 ``