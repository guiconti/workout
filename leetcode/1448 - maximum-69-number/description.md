Given a positive integer `` num `` consisting only of digits 6 and 9.

Return the maximum number you can get by changing __at most__ one digit (6 becomes 9, and 9 becomes 6).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = 9669
<strong>Output:</strong> 9969
<strong>Explanation:</strong> 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.&nbsp;
The maximum number is 9969.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = 9996
<strong>Output:</strong> 9999
<strong>Explanation:</strong> Changing the last digit 6 to 9 results in the maximum number.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> num = 9999
<strong>Output:</strong> 9999
<strong>Explanation:</strong> It is better not to apply any change.</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= num &lt;= 10^4 ``
*   `` num ``'s digits are 6 or 9.