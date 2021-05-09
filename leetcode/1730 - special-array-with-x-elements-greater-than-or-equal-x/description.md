You are given an array `` nums `` of non-negative integers. `` nums `` is considered __special__ if there exists a number `` x `` such that there are __exactly__ `` x `` numbers in `` nums `` that are __greater than or equal to__ `` x ``.

Notice that `` x `` __does not__ have to be an element in `` nums ``.

Return `` x `` _if the array is __special__, otherwise, return _`` -1 ``. It can be proven that if `` nums `` is special, the value for `` x `` is __unique__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 values (3 and 5) that are greater than or equal to 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0,0]
<strong>Output:</strong> -1
<strong>Explanation:</strong> No numbers fit the criteria for x.
If x = 0, there should be 0 numbers &gt;= x, but there are 2.
If x = 1, there should be 1 number &gt;= x, but there are 0.
If x = 2, there should be 2 numbers &gt;= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [0,4,3,0,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 values that are greater than or equal to 3.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [3,6,7,7,0]
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 100 ``
*   `` 0 &lt;= nums[i] &lt;= 1000 ``