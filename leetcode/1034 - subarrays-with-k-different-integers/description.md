Given an array `` A `` of positive integers, call a (contiguous, not necessarily distinct) subarray of `` A `` _good_ if the number of different integers in that subarray is exactly `` K ``.

(For example, `` [1,2,3,1,2] `` has `` 3 `` different integers: `` 1 ``, `` 2 ``, and `` 3 ``.)

Return the number of good subarrays of `` A ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,2,1,2,3]</span>, K = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">7</span>
<strong>Explanation: </strong>Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,2,1,3,4]</span>, K = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= A.length &lt;= 20000 ``
2.   `` 1 &lt;= A[i] &lt;= A.length ``
3.   `` 1 &lt;= K &lt;= A.length ``