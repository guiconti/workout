Given an array `` A `` of non-negative integers, the array is _squareful_ if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.&nbsp; Two permutations `` A1 `` and `` A2 `` differ if and only if there is some index `` i `` such that `` A1[i] != A2[i] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,17,8]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
[1,8,17] and [17,8,1] are the valid permutations.
</pre>

__Example 2:__

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,2,2]</span>
<strong>Output: </strong><span id="example-output-2">1</span>
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= A.length &lt;= 12 ``
2.   `` 0 &lt;= A[i] &lt;= 1e9 ``