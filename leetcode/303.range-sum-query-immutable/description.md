Given an integer array `` nums ``, handle multiple queries of the following type:

1.   Calculate the __sum__ of the elements of `` nums `` between indices `` left `` and `` right `` __inclusive__ where `` left &lt;= right ``.

Implement the `` NumArray `` class:

*   `` NumArray(int[] nums) `` Initializes the object with the integer array `` nums ``.
*   `` int sumRange(int left, int right) `` Returns the __sum__ of the elements of `` nums `` between indices `` left `` and `` right `` __inclusive__ (i.e. `` nums[left] + nums[left + 1] + ... + nums[right] ``).

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
<strong>Output</strong>
[null, 1, -1, -3]

<strong>Explanation</strong>
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code>
*   `` 0 &lt;= left &lt;= right &lt; nums.length ``
*   At most <code>10<sup>4</sup></code> calls will be made to `` sumRange ``.