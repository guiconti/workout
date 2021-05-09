Given two integer arrays&nbsp;`` arr1 `` and `` arr2 ``, return the minimum number of operations (possibly zero) needed&nbsp;to make `` arr1 `` strictly increasing.

In one operation, you can choose two indices&nbsp;`` 0 &lt;=&nbsp;i &lt; arr1.length ``&nbsp;and&nbsp;`` 0 &lt;= j &lt; arr2.length ``&nbsp;and do the assignment&nbsp;`` arr1[i] = arr2[j] ``.

If there is no way to make&nbsp;`` arr1 ``&nbsp;strictly increasing,&nbsp;return&nbsp;`` -1 ``.

&nbsp;

__Example 1:__

<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
    <strong>Output:</strong> 1
    <strong>Explanation:</strong> Replace 5 with <code>2</code>, then <code>arr1 = [1, 2, 3, 6, 7]</code>.

__Example 2:__

<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [4,3,1]
    <strong>Output:</strong> 2
    <strong>Explanation:</strong> Replace 5 with <code>3</code> and then replace <code>3</code> with <code>4</code>. <code>arr1 = [1, 3, 4, 6, 7]</code>.

__Example 3:__

<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
    <strong>Output:</strong> -1
    <strong>Explanation:</strong> You can't make arr1 strictly increasing.

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr1.length, arr2.length &lt;= 2000 ``
*   `` 0 &lt;= arr1[i], arr2[i] &lt;= 10^9 ``

&nbsp;