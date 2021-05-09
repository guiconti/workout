Given an integer array `` nums ``, return _the maximum difference between two successive elements in its sorted form_. If the array contains less than two elements, return `` 0 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,6,9,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The array contains less than 2 elements, therefore return 0.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code>

&nbsp;
__Follow up:__ Could you solve it in linear time/space?