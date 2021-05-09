Given an array&nbsp;of `` n `` integers `` nums ``, a __132 pattern__ is a subsequence of three integers `` nums[i] ``, `` nums[j] `` and `` nums[k] `` such that `` i &lt; j &lt; k `` and `` nums[i] &lt; nums[k] &lt; nums[j] ``.

Return _`` true `` if there is a __132 pattern__ in `` nums ``, otherwise, return `` false ``._

__Follow up: __The `` O(n^2) `` is trivial, could you come up with the `` O(n logn) `` or the `` O(n) `` solution?

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no 132 pattern in the sequence.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [3,1,4,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a 132 pattern in the sequence: [1, 4, 2].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [-1,3,2,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
</pre>

&nbsp;

__Constraints:__

*   `` n == nums.length ``
*   <code>1 &lt;= n &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>