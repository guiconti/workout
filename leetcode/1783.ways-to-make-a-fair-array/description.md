You are given an integer array&nbsp;`` nums ``. You can choose __exactly one__ index (__0-indexed__) and remove the element. Notice that the index of the elements may change after the removal.

For example, if `` nums = [6,1,7,4,1] ``:

*   Choosing to remove index `` 1 `` results in `` nums = [6,7,4,1] ``.
*   Choosing to remove index `` 2 `` results in `` nums = [6,1,4,1] ``.
*   Choosing to remove index `` 4 `` results in `` nums = [6,1,7,4] ``.

An array is __fair__ if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the ___number__ of indices that you could choose such that after the removal, _`` nums ``_ __is __fair__. _

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,1,6,4]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Remove index 0: [1,6,4] -&gt; Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -&gt; Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -&gt; Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -&gt; Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong>&nbsp;You can remove any index and the remaining array is fair.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;You cannot make a fair array after removing any index.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code>