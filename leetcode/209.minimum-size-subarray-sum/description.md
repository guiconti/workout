Given an array of positive integers `` nums `` and a positive integer `` target ``, return the minimal length of a __contiguous subarray__ <code>[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]</code> of which the sum is greater than or equal to `` target ``. If there is no such subarray, return `` 0 `` instead.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> target = 7, nums = [2,3,1,2,4,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The subarray [4,3] has the minimal length under the problem constraint.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> target = 4, nums = [1,4,4]
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= target &lt;= 10<sup>9</sup></code>
*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code>

&nbsp;
__Follow up:__ If you have figured out the `` O(n) `` solution, try coding another solution of which the time complexity is `` O(n log(n)) ``.