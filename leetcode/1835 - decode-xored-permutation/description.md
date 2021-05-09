There is an integer array `` perm `` that is a permutation of the first `` n `` positive integers, where `` n `` is always __odd__.

It was encoded into another integer array `` encoded `` of length `` n - 1 ``, such that `` encoded[i] = perm[i] XOR perm[i + 1] ``. For example, if `` perm = [1,3,2] ``, then `` encoded = [2,1] ``.

Given the `` encoded `` array, return _the original array_ `` perm ``. It is guaranteed that the answer exists and is unique.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> encoded = [3,1]
<strong>Output:</strong> [1,2,3]
<strong>Explanation:</strong> If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> encoded = [6,5,4,6]
<strong>Output:</strong> [2,4,1,5,3]
</pre>

&nbsp;

__Constraints:__

*   <code>3 &lt;= n &lt;&nbsp;10<sup>5</sup></code>
*   `` n ``&nbsp;is odd.
*   `` encoded.length == n - 1 ``