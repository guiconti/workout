Given an integer array `` nums ``, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in __any order__.

__Follow up:&nbsp;__Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,1,3,2,5]
<strong>Output:</strong> [3,5]
<strong>Explanation: </strong> [5, 3] is also a valid answer.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-1,0]
<strong>Output:</strong> [-1,0]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [1,0]
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code>
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>
*   Each integer in `` nums `` will appear twice, only two integers will appear once.