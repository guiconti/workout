You are given an array of __distinct__ integers `` arr `` and an array of integer arrays `` pieces ``, where the integers in `` pieces `` are __distinct__. Your goal is to form `` arr `` by concatenating the arrays in `` pieces `` __in any order__. However, you are __not__ allowed to reorder the integers in each array `` pieces[i] ``.

Return `` true `` _if it is possible __to form the array _`` arr ``_ from _`` pieces ``. Otherwise, return `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [85], pieces = [[85]]
<strong>Output:</strong> true
</pre>

__Example 2:__

<strong>Input:</strong> arr = [15,88], pieces = [[88],[15]]
    <strong>Output:</strong> true
    <strong>Explanation:</strong> Concatenate [15] then <code>[88]</code>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [49,18,16], pieces = [[16,18,49]]
<strong>Output:</strong> false
<strong>Explanation:</strong> Even though the numbers match, we cannot reorder pieces[0].
</pre>

__Example 4:__

<strong>Input:</strong> arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
    <strong>Output:</strong> true
    <strong>Explanation:</strong> Concatenate [91] then <code>[4,64]</code> then <code>[78]</code>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [1,3,5,7], pieces = [[2,4,6,8]]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= pieces.length &lt;= arr.length &lt;= 100 ``
*   `` sum(pieces[i].length) == arr.length ``
*   `` 1 &lt;= pieces[i].length &lt;= arr.length ``
*   `` 1 &lt;= arr[i], pieces[i][j] &lt;= 100 ``
*   The integers in&nbsp;`` arr ``&nbsp;are __distinct__.
*   The integers in&nbsp;`` pieces `` are __distinct__&nbsp;(i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).