Given two arrays `` arr1 `` and `` arr2 ``, the elements of `` arr2 `` are distinct, and all elements in `` arr2 `` are also in `` arr1 ``.

Sort the elements of `` arr1 `` such that the relative ordering of items in `` arr1 `` are the same as in `` arr2 ``.&nbsp; Elements that don't appear in `` arr2 `` should be placed at the end of `` arr1 `` in __ascending__ order.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
<strong>Output:</strong> [2,2,2,1,4,3,3,9,6,7,19]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr1.length, arr2.length &lt;= 1000 ``
*   `` 0 &lt;= arr1[i], arr2[i] &lt;= 1000 ``
*   All the elements of `` arr2 `` are __distinct__.
*   Each&nbsp;`` arr2[i] `` is in `` arr1 ``.