You are given an integer array `` nums ``.

You should move each element of `` nums `` into one of the two arrays `` A `` and `` B `` such that `` A `` and `` B `` are non-empty, and `` average(A) == average(B) ``.

Return `` true `` if it is possible to achieve that and `` false `` otherwise.

__Note__ that for an array `` arr ``, `` average(arr) `` is the sum of all the elements of `` arr `` over the length of `` arr ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5,6,7,8]
<strong>Output:</strong> true
<strong>Explanation:</strong> We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [3,1]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 30 ``
*   <code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code>