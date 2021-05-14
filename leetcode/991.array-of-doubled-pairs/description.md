Given an array of integers `` arr `` of even length, return `` true `` if and only if it is possible to reorder it such that `` arr[2 * i + 1] = 2 * arr[2 * i] `` for every `` 0 &lt;= i &lt; len(arr) / 2 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,1,3,6]
<strong>Output:</strong> false
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [2,1,2,6]
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [4,-2,2,-4]
<strong>Output:</strong> true
<strong>Explanation:</strong> We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [1,2,4,16,8,4]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   <code>0 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code>
*   `` arr.length `` is even.
*   <code>-10<sup>5</sup> &lt;= arr[i] &lt;= 10<sup>5</sup></code>