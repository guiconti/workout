We are given a list `` nums `` of integers representing a list compressed with run-length encoding.

Consider each adjacent pair&nbsp;of elements `` [freq, val] = [nums[2*i], nums[2*i+1]] ``&nbsp;(with `` i &gt;= 0 ``).&nbsp; For each such pair, there are `` freq `` elements with value `` val `` concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [2,4,4,4]
<strong>Explanation:</strong> The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1,1,2,3]
<strong>Output:</strong> [1,3,3]
</pre>

&nbsp;

__Constraints:__

<ul><li><code>2 &lt;= nums.length &lt;= 100</code></li><li><code>nums.length % 2 == 0</code></li><li><code><font face="monospace">1 &lt;= nums[i] &lt;= 100</font></code></li></ul>