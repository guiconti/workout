A split of an integer array is __good__ if:

*   The array is split into three __non-empty__ contiguous subarrays - named `` left ``, `` mid ``, `` right `` respectively from left to right.
*   The sum of the elements in `` left `` is less than or equal to the sum of the elements in `` mid ``, and the sum of the elements in `` mid `` is less than or equal to the sum of the elements in `` right ``.

Given `` nums ``, an array of __non-negative__ integers, return _the number of __good__ ways to split_ `` nums ``. As the number may be too large, return it __modulo__ <code>10<sup>9 </sup>+ 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only good way to split nums is [1] [1] [1].</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,2,2,2,5,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no good way to split nums.</pre>

&nbsp;

__Constraints:__

*   <code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code>