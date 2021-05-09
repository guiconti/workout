Given a __sorted__ integer array `` arr ``, two integers `` k `` and `` x ``, return the `` k `` closest integers to `` x `` in the array. The result should also be sorted in ascending order.

An integer `` a `` is closer to `` x `` than an integer `` b `` if:

*   `` |a - x| &lt; |b - x| ``, or
*   `` |a - x| == |b - x| `` and `` a &lt; b ``

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = 3
<strong>Output:</strong> [1,2,3,4]
</pre>

__Example 2:__

<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = -1
<strong>Output:</strong> [1,2,3,4]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= k &lt;= arr.length ``
*   <code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code>
*   `` arr `` is sorted in __ascending__ order.
*   <code>-10<sup>4</sup> &lt;= arr[i], x &lt;= 10<sup>4</sup></code>