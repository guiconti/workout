You are given an integer array `` nums `` (__0-indexed__). In one operation, you can choose an element of the array and increment it by `` 1 ``.

*   For example, if `` nums = [1,2,3] ``, you can choose to increment `` nums[1] `` to make <code>nums = [1,<u><b>3</b></u>,3]</code>.

Return _the __minimum__ number of operations needed to make_ `` nums `` ___strictly__ __increasing__._

An array `` nums `` is __strictly increasing__ if `` nums[i] &lt; nums[i+1] `` for all `` 0 &lt;= i &lt; nums.length - 1 ``. An array of length `` 1 `` is trivially strictly increasing.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,<u><strong>2</strong></u>].
2) Increment nums[1], so nums becomes [1,<u><strong>2</strong></u>,2].
3) Increment nums[2], so nums becomes [1,2,<u><strong>3</strong></u>].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,5,2,4,1]
<strong>Output:</strong> 14
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [8]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 5000 ``
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>