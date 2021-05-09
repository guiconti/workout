Given an array of integers `` arr `` and an integer `` target ``.

You have to find __two non-overlapping sub-arrays__ of `` arr `` each with a sum equal `` target ``. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is __minimum__.

Return _the minimum sum of the lengths_ of the two required sub-arrays, or return `` -1 `` if you cannot find such two sub-arrays.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,2,2,4,3], target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [7,3,4,7], target = 7
<strong>Output:</strong> 2
<strong>Explanation:</strong> Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [4,3,2,6,2,3,4], target = 6
<strong>Output:</strong> -1
<strong>Explanation:</strong> We have only one sub-array of sum = 6.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [5,5,4,4,5], target = 3
<strong>Output:</strong> -1
<strong>Explanation:</strong> We cannot find a sub-array of sum = 3.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [3,1,1,1,5,1,2,1], target = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> Note that sub-arrays [1,2] and [2,1] cannot be an answer because they overlap.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code>
*   `` 1 &lt;= arr[i] &lt;= 1000 ``
*   <code>1 &lt;= target &lt;= 10<sup>8</sup></code>