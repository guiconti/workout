Given an array `` nums `` of&nbsp;positive integers. Your task is to select some subset of `` nums ``, multiply each element by an integer and add all these numbers.&nbsp;The array is said to be&nbsp;__good&nbsp;__if you can obtain a sum of&nbsp;`` 1 ``&nbsp;from the array by any possible subset and multiplicand.

Return&nbsp;`` True ``&nbsp;if the array is __good&nbsp;__otherwise&nbsp;return&nbsp;`` False ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [12,5,7,23]
<strong>Output:</strong> true
<strong>Explanation:</strong> Pick numbers 5 and 7.
5*3 + 7*(-2) = 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [29,6,10]
<strong>Output:</strong> true
<strong>Explanation:</strong> Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [3,6]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 10^5 ``
*   `` 1 &lt;= nums[i] &lt;= 10^9 ``