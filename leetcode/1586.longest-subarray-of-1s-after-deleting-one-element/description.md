Given a binary array `` nums ``, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's&nbsp;in the resulting array.

Return 0 if there is no such subarray.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,1,0,1]
<strong>Output:</strong> 3
<strong>Explanation: </strong>After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0,1,1,1,0,1,1,0,1]
<strong>Output:</strong> 5
<strong>Explanation: </strong>After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 2
<strong>Explanation: </strong>You must delete one element.</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [1,1,0,0,1,1,1,0,1]
<strong>Output:</strong> 4
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10^5 ``
*   `` nums[i] ``&nbsp;is either&nbsp;`` 0 ``&nbsp;or&nbsp;`` 1 ``.