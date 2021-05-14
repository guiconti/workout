Given two numbers `` arr1 `` and `` arr2 `` in base __-2__, return the result of adding them together.

Each number is given in _array format_:&nbsp; as an array of 0s and 1s, from most significant bit to least significant bit.&nbsp; For example, `` arr = [1,1,0,1] `` represents the number `` (-2)^3&nbsp;+ (-2)^2 + (-2)^0 = -3 ``.&nbsp; A number `` arr `` in _array, format_ is also guaranteed to have no leading zeros: either&nbsp;`` arr == [0] `` or `` arr[0] == 1 ``.

Return the result of adding `` arr1 `` and `` arr2 `` in the same format: as an array of 0s and 1s with no leading zeros.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr1 = [1,1,1,1,1], arr2 = [1,0,1]
<strong>Output:</strong> [1,0,0,0,0]
<strong>Explanation: </strong>arr1 represents 11, arr2 represents 5, the output represents 16.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr1 = [0], arr2 = [0]
<strong>Output:</strong> [0]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr1 = [0], arr2 = [1]
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr1.length,&nbsp;arr2.length &lt;= 1000 ``
*   `` arr1[i] ``&nbsp;and `` arr2[i] `` are&nbsp;`` 0 `` or `` 1 ``
*   `` arr1 `` and `` arr2 `` have no leading zeros