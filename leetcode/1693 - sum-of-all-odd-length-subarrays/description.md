Given an array of positive integers&nbsp;`` arr ``, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous&nbsp;subsequence of the array.

Return&nbsp;_the sum of all odd-length subarrays of&nbsp;_`` arr ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,4,2,5,3]
<strong>Output:</strong> 58
<strong>Explanation: </strong>The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,2]
<strong>Output:</strong> 3
<b>Explanation: </b>There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [10,11,12]
<strong>Output:</strong> 66
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 100 ``
*   `` 1 &lt;= arr[i] &lt;= 1000 ``