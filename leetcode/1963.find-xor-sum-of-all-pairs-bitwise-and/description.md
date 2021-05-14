The __XOR sum__ of a list is the bitwise `` XOR `` of all its elements. If the list only contains one element, then its __XOR sum__ will be equal to this element.

*   For example, the __XOR sum__ of `` [1,2,3,4] `` is equal to `` 1 XOR 2 XOR 3 XOR 4 = 4 ``, and the __XOR sum__ of `` [3] `` is equal to `` 3 ``.

You are given two __0-indexed__ arrays `` arr1 `` and `` arr2 `` that consist only of non-negative integers.

Consider the list containing the result of `` arr1[i] AND arr2[j] `` (bitwise `` AND ``) for every `` (i, j) `` pair where `` 0 &lt;= i &lt; arr1.length `` and `` 0 &lt;= j &lt; arr2.length ``.

Return _the __XOR sum__ of the aforementioned list_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr1 = [1,2,3], arr2 = [6,5]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The list = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1].
The XOR sum = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr1 = [12], arr2 = [4]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The list = [12 AND 4] = [4]. The XOR sum = 4.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr1.length, arr2.length &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= arr1[i], arr2[j] &lt;= 10<sup>9</sup></code>