Given an array of positive integers `` arr `` (not necessarily distinct), return _the lexicographically largest permutation that is smaller than_ `` arr ``, that can be __made with exactly one swap__ (A _swap_ exchanges the positions of two numbers `` arr[i] `` and `` arr[j] ``). If it cannot be done, then return the same array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,2,1]
<strong>Output:</strong> [3,1,2]
<strong>Explanation:</strong> Swapping 2 and 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,1,5]
<strong>Output:</strong> [1,1,5]
<strong>Explanation:</strong> This is already the smallest permutation.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,9,4,6,7]
<strong>Output:</strong> [1,7,4,6,9]
<strong>Explanation:</strong> Swapping 9 and 7.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [3,1,1,3]
<strong>Output:</strong> [1,3,1,3]
<strong>Explanation:</strong> Swapping 1 and 3.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code>
*   <code>1 &lt;= arr[i] &lt;= 10<sup>4</sup></code>