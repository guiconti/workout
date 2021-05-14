Given two arrays of integers with equal lengths, return the maximum value of:

`` |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j| ``

where the maximum is taken over all `` 0 &lt;= i, j &lt; arr1.length ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
<strong>Output:</strong> 13
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
<strong>Output:</strong> 20
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= arr1.length == arr2.length &lt;= 40000 ``
*   `` -10^6 &lt;= arr1[i], arr2[i] &lt;= 10^6 ``