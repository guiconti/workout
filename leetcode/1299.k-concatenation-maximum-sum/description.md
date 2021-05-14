Given an integer array `` arr `` and an integer `` k ``, modify the array by repeating it `` k `` times.

For example, if `` arr = [1, 2] `` and `` k = 3  ``then the modified array will be `` [1, 2, 1, 2, 1, 2] ``.

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be `` 0 `` and its sum in that case is `` 0 ``.

As the answer can be very large, return the answer __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,2], k = 3
<strong>Output:</strong> 9
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,-2,1], k = 5
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [-1,-2], k = 7
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= k &lt;= 10<sup>5</sup></code>
*   <code>-10<sup>4</sup> &lt;= arr[i] &lt;= 10<sup>4</sup></code>