Given an array `` nums `` of integers, you can perform operations on the array.

In each operation, you pick any `` nums[i] `` and delete it to earn `` nums[i] `` points. After, you must delete __every__ element equal to `` nums[i] - 1 `` or `` nums[i] + 1 ``.

You start with `` 0 `` points. Return the maximum number of points you can earn by applying such operations.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,4,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points.
6 total points are earned.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,2,3,3,3,4]
<strong>Output:</strong> 9
<strong>Explanation:</strong> Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>