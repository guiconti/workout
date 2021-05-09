Given an array of integers `` nums `` and an integer `` target ``.

Return the number of __non-empty__ subsequences of `` nums `` such that the sum of the minimum and maximum element on it is less or equal to&nbsp;`` target ``. Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;<code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,5,6,7], target = 9
<strong>Output:</strong> 4
<strong>Explanation: </strong>There are 4 subsequences that satisfy the condition.
[3] -&gt; Min value + max value &lt;= target (3 + 3 &lt;= 9)
[3,5] -&gt; (3 + 5 &lt;= 9)
[3,5,6] -&gt; (3 + 6 &lt;= 9)
[3,6] -&gt; (3 + 6 &lt;= 9)
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [3,3,6,8], target = 10
<strong>Output:</strong> 6
<strong>Explanation: </strong>There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [2,3,3,4,6,7], target = 12
<strong>Output:</strong> 61
<strong>Explanation: </strong>There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [5,2,4,1,7,6,8], target = 16
<strong>Output:</strong> 127
<strong>Explanation: </strong>All non-empty subset satisfy the condition (2^7 - 1) = 127</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code>
*   <code>1 &lt;= target &lt;= 10<sup>6</sup></code>