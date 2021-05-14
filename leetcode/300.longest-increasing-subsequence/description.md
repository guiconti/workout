Given an integer array `` nums ``, return the length of the longest strictly increasing subsequence.

A __subsequence__ is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `` [3,6,2,7] `` is a subsequence of the array `` [0,3,1,6,2,2,7] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [10,9,2,5,3,7,101,18]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0,1,0,3,2,3]
<strong>Output:</strong> 4
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [7,7,7,7,7,7,7]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 2500 ``
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>

&nbsp;

__Follow up:__

*   Could you come up with the <code>O(n<sup>2</sup>)</code> solution?
*   Could you improve it to `` O(n log(n)) `` time complexity?