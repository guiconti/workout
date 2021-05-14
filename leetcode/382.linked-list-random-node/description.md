Given a singly linked list, return a random node's value from the linked list. Each node must have the __same probability__ of being chosen.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg" style="width: 302px; height: 62px;"/>

<pre>
<strong>Input</strong>
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
<strong>Output</strong>
[null, 1, 3, 2, 2, 3]

<strong>Explanation</strong>
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
</pre>

&nbsp;

__Constraints:__

*   The number of nodes in the linked list will be in the range <code>[1, 10<sup>4</sup>]</code>.
*   <code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code>
*   At most <code>10<sup>4</sup></code> calls will be made to `` getRandom ``.

&nbsp;

__Follow up:__

*   What if the linked list is extremely large and its length is unknown to you?
*   Could you solve this efficiently without using extra space?