Given an integer array&nbsp;`` arr ``, remove a&nbsp;subarray (can be empty) from&nbsp;`` arr ``&nbsp;such that the remaining elements in `` arr ``&nbsp;are __non-decreasing__.

A subarray is a contiguous&nbsp;subsequence of the array.

Return&nbsp;_the length of the shortest subarray to remove_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,2,3,10,4,2,3,5]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [5,4,3,2,1]
<strong>Output:</strong> 4
<strong>Explanation: </strong>Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation: </strong>The array is already non-decreasing. We do not need to remove any elements.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [1]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 10^5 ``
*   `` 0 &lt;= arr[i] &lt;= 10^9 ``