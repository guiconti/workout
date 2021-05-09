Given an array of integers `` nums `` and an integer `` threshold ``, we will choose a positive integer `` divisor ``, divide all the array by it, and sum the division's result. Find the __smallest__ `` divisor `` such that the result mentioned above is less than or equal to `` threshold ``.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: `` 7/3 = 3 `` and `` 10/2 = 5 ``).

It is guaranteed that there will be an answer.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,5,9], threshold = 6
<strong>Output:</strong> 5
<strong>Explanation:</strong> We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [44,22,33,11,1], threshold = 5
<strong>Output:</strong> 44
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [21212,10101,12121], threshold = 1000000
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [2,3,5,7,11], threshold = 11
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code>
*   <code>nums.length &lt;= threshold &lt;= 10<sup>6</sup></code>