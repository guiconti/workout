Given a circular integer array `` nums `` (i.e., the next element of `` nums[nums.length - 1] `` is `` nums[0] ``), return _the __next greater number__ for every element in_ `` nums ``.

The __next greater number__ of a number `` x `` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `` -1 `` for this number.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,3]
<strong>Output:</strong> [2,3,4,-1,4]
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>