Given an array `` nums `` of integers, return how many of them contain an __even number__ of digits.
&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [12,345,2,6,7896]
<strong>Output:</strong> 2
<strong>Explanation: 
</strong>12 contains 2 digits (even number of digits).&nbsp;
345 contains 3 digits (odd number of digits).&nbsp;
2 contains 1 digit (odd number of digits).&nbsp;
6 contains 1 digit (odd number of digits).&nbsp;
7896 contains 4 digits (even number of digits).&nbsp;
Therefore only 12 and 7896 contain an even number of digits.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [555,901,482,1771]
<strong>Output:</strong> 1 
<strong>Explanation: </strong>
Only 1771 contains an even number of digits.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 500 ``
*   `` 1 &lt;= nums[i] &lt;= 10^5 ``