We have an array `` arr `` of non-negative integers.

For every (contiguous) subarray `` sub = [arr[i], arr[i + 1], ..., arr[j]] `` (with `` i &lt;= j ``), we take the bitwise OR of all the elements in `` sub ``, obtaining a result `` arr[i] | arr[i + 1] | ... | arr[j] ``.

Return the number of possible results. Results that occur more than once are only counted once in the final answer

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is only one possible result: 0.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,1,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [1,2,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The possible results are 1, 2, 3, 4, 6, and 7.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code>
*   <code>0 &lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code>