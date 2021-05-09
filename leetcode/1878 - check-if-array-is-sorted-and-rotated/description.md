Given an array `` nums ``, return `` true ``_ if the array was originally sorted in non-decreasing order, then rotated __some__ number of positions (including zero)_. Otherwise, return `` false ``.

There may be __duplicates__ in the original array.

__Note:__ An array `` A `` rotated by `` x `` positions results in an array `` B `` of the same length such that `` A[i] == B[(i+x) % A.length] ``, where `` % `` is the modulo operation.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,1,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no sorted array once rotated that can make nums.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> true
<strong>Explanation:</strong> [1,1,1] is the original sorted array.
You can rotate any number of positions to make nums.
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums = [2,1]
<strong>Output:</strong> true
<strong>Explanation:</strong> [1,2] is the original sorted array.
You can rotate the array by x = 5 positions to begin on the element of value 2: [2,1].
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 100 ``
*   `` 1 &lt;= nums[i] &lt;= 100 ``