There is a __hidden__ integer array `` arr `` that consists of `` n `` non-negative integers.

It was encoded into another integer array `` encoded `` of length `` n - 1 ``, such that `` encoded[i] = arr[i] XOR arr[i + 1] ``. For example, if `` arr = [1,0,2,1] ``, then `` encoded = [1,2,3] ``.

You are given the `` encoded `` array. You are also given an integer `` first ``, that is the first element of `` arr ``, i.e. `` arr[0] ``.

Return _the original array_ `` arr ``. It can be proved that the answer exists and is unique.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> encoded = [1,2,3], first = 1
<strong>Output:</strong> [1,0,2,1]
<strong>Explanation:</strong> If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> encoded = [6,2,7,3], first = 4
<strong>Output:</strong> [4,2,0,7,4]
</pre>

&nbsp;

__Constraints:__

*   <code>2 &lt;= n &lt;= 10<sup>4</sup></code>
*   `` encoded.length == n - 1 ``
*   <code>0 &lt;= encoded[i] &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= first &lt;= 10<sup>5</sup></code>