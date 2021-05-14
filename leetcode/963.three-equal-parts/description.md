You are given an array `` arr `` which consists of only zeros and ones, divide the array into __three non-empty parts__ such that all of these parts represent the same binary value.

If it is possible, return any `` [i, j] `` with `` i + 1 &lt; j ``, such that:

*   `` arr[0], arr[1], ..., arr[i] `` is the first part,
*   `` arr[i + 1], arr[i + 2], ..., arr[j - 1] `` is the second part, and
*   `` arr[j], arr[j + 1], ..., arr[arr.length - 1] `` is the third part.
*   All three parts have equal binary values.

If it is not possible, return `` [-1, -1] ``.

Note that the entire part is used when considering what binary value it represents. For example, `` [1,1,0] `` represents `` 6 `` in decimal, not `` 3 ``. Also, leading zeros __are allowed__, so `` [0,1,1] `` and `` [1,1] `` represent the same value.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> arr = [1,0,1,0,1]
<strong>Output:</strong> [0,3]
</pre>

__Example 2:__

<pre><strong>Input:</strong> arr = [1,1,0,1,1]
<strong>Output:</strong> [-1,-1]
</pre>

__Example 3:__

<pre><strong>Input:</strong> arr = [1,1,0,0,1]
<strong>Output:</strong> [0,2]
</pre>

&nbsp;

__Constraints:__

*   <code>3 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code>
*   `` arr[i] `` is `` 0 `` or `` 1 ``