Given two integer arrays of equal length `` target `` and `` arr ``.

In one step, you can select any __non-empty sub-array__ of `` arr `` and reverse it. You are allowed to make any number of steps.

Return _True_ if you can make `` arr `` equal to `` target ``, or _False_ otherwise.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> target = [1,2,3,4], arr = [2,4,1,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> target = [7], arr = [7]
<strong>Output:</strong> true
<strong>Explanation:</strong> arr is equal to target without any reverses.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> target = [1,12], arr = [12,1]
<strong>Output:</strong> true
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> target = [3,7,9], arr = [3,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> arr doesn't have value 9 and it can never be converted to target.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> target = [1,1,1,1,1], arr = [1,1,1,1,1]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` target.length == arr.length ``
*   `` 1 &lt;= target.length &lt;= 1000 ``
*   `` 1 &lt;= target[i] &lt;= 1000 ``
*   `` 1 &lt;= arr[i] &lt;= 1000 ``