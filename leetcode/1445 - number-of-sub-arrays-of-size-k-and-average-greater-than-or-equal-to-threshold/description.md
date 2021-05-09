Given an array of integers `` arr `` and two integers `` k `` and `` threshold ``.

Return _the number of sub-arrays_ of size `` k `` and average greater than or equal to `` threshold ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,1,1,1,1], k = 1, threshold = 0
<strong>Output:</strong> 5
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
<strong>Output:</strong> 6
<strong>Explanation:</strong> The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
<strong>Output:</strong> 1
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [4,4,4,4], k = 4, threshold = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 10^5 ``
*   `` 1 &lt;= arr[i] &lt;= 10^4 ``
*   `` 1 &lt;= k &lt;= arr.length ``
*   `` 0 &lt;= threshold &lt;= 10^4 ``