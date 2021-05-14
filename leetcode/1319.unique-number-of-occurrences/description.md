Given an array of integers `` arr ``,&nbsp;write a function that returns `` true `` if and only if the number of occurrences of each value in the array is unique.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,2,2,1,1,3]
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,2]
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [-3,0,1,-3,1,1,1,-3,10,0]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length&nbsp;&lt;= 1000 ``
*   `` -1000 &lt;= arr[i] &lt;= 1000 ``