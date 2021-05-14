Given an integer array `` arr ``, partition the array into (contiguous) subarrays of length __at most__ `` k ``. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return _the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a __32-bit__ integer._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,15,7,9,2,5,10], k = 3
<strong>Output:</strong> 84
<strong>Explanation:</strong> arr becomes [15,15,15,9,10,10,10]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
<strong>Output:</strong> 83
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1], k = 1
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 500 ``
*   <code>0 &lt;= arr[i] &lt;= 10<sup>9</sup></code>
*   `` 1 &lt;= k &lt;= arr.length ``