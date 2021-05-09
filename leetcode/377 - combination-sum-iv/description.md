Given an array of __distinct__ integers `` nums `` and a target integer `` target ``, return _the number of possible combinations that add up to_&nbsp;`` target ``.

The answer is __guaranteed__ to fit in a __32-bit__ integer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3], target = 4
<strong>Output:</strong> 7
<strong>Explanation:</strong>
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [9], target = 3
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 200 ``
*   `` 1 &lt;= nums[i] &lt;= 1000 ``
*   All the elements of `` nums `` are __unique__.
*   `` 1 &lt;= target &lt;= 1000 ``

&nbsp;

__Follow up:__ What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?