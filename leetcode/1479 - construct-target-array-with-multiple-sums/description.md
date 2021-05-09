Given an array of integers&nbsp;`` target ``. From a starting array, `` A ``&nbsp;consisting of all 1's, you may perform the following procedure :

*   let `` x `` be the sum of all elements currently in your array.
*   choose index `` i ``, such that&nbsp;`` 0 &lt;= i &lt; target.size `` and set the value of `` A `` at index `` i `` to `` x ``.
*   You may repeat this procedure&nbsp;as many times as needed.

Return True if it is possible to construct the `` target `` array from `` A `` otherwise&nbsp;return False.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> target = [9,3,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> target = [1,1,1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> Impossible to create target array from [1,1,1,1].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> target = [8,5]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   `` N == target.length ``
*   `` 1 &lt;= target.length&nbsp;&lt;= 5 * 10^4 ``
*   `` 1 &lt;= target[i] &lt;= 10^9 ``