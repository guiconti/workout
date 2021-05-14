You are playing a game involving a __circular__ array of non-zero integers `` nums ``. Each `` nums[i] `` denotes the number of indices forward/backward you must move if you are located at index `` i ``:

*   If `` nums[i] `` is positive, move `` nums[i] `` steps __forward__, and
*   If `` nums[i] `` is negative, move `` nums[i] `` steps __backward__.

Since the array is __circular__, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A __cycle__ in the array consists of a sequence of indices `` seq `` of length `` k `` where:

*   Following the movement rules above results in the repeating index sequence `` seq[0] -&gt; seq[1] -&gt; ... -&gt; seq[k - 1] -&gt; seq[0] -&gt; ... ``
*   Every `` nums[seq[j]] `` is either __all positive__ or __all negative__.
*   `` k &gt; 1 ``

Return `` true ``_ if there is a __cycle__ in _`` nums ``_, or _`` false ``_ otherwise_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,-1,1,2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong>
There is a cycle from index 0 -&gt; 2 -&gt; 3 -&gt; 0 -&gt; ...
The cycle's length is 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [-1,2]
<strong>Output:</strong> false
<strong>Explanation:</strong>
The sequence from index 1 -&gt; 1 -&gt; 1 -&gt; ... is not a cycle because the sequence's length is 1.
By definition the sequence's length must be strictly greater than 1 to be a cycle.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [-2,1,-1,-2,-2]
<strong>Output:</strong> false
<strong>Explanation:</strong>
The sequence from index 1 -&gt; 2 -&gt; 1 -&gt; ... is not a cycle because nums[1] is positive, but nums[2] is negative.
Every nums[seq[j]] must be either all positive or all negative.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= nums.length &lt;= 5000 ``
*   `` -1000 &lt;= nums[i] &lt;= 1000 ``
*   `` nums[i] != 0 ``

&nbsp;

__Follow up:__ Could you solve it in `` O(n) `` time complexity and `` O(1) `` extra space complexity?