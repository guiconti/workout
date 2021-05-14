Given an integer array&nbsp;`` arr `` and a target value `` target ``, return&nbsp;the integer&nbsp;`` value ``&nbsp;such that when we change all the integers&nbsp;larger than `` value ``&nbsp;in the given array to be equal to&nbsp;`` value ``,&nbsp;the sum of the array gets&nbsp;as close as possible (in absolute difference) to&nbsp;`` target ``.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from `` arr ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [4,9,3], target = 10
<strong>Output:</strong> 3
<strong>Explanation:</strong> When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [2,3,5], target = 10
<strong>Output:</strong> 5
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [60864,25176,27249,21296,20204], target = 56803
<strong>Output:</strong> 11361
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 10^4 ``
*   `` 1 &lt;= arr[i], target &lt;= 10^5 ``