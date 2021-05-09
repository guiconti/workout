Given an integer array `` nums `` with possible __duplicates__, randomly output the index of a given `` target `` number. You can assume that the given target number must exist in the array.

Implement the `` Solution `` class:

*   `` Solution(int[] nums) `` Initializes the object with the array `` nums ``.
*   `` int pick(int target) `` Picks a random index `` i `` from `` nums `` where `` nums[i] == target ``. If there are multiple valid i's, then each index should have an equal probability of returning.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
<strong>Output</strong>
[null, 4, 0, 2]

<strong>Explanation</strong>
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code>
*   <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>
*   `` target `` is an integer from `` nums ``.
*   At most <code>10<sup>4</sup></code> calls will be made to `` pick ``.