Given an integer array `` nums ``, handle multiple queries of the following types:

1.   __Update__ the value of an element in `` nums ``.
2.   Calculate the __sum__ of the elements of `` nums `` between indices `` left `` and `` right `` __inclusive__ where `` left &lt;= right ``.

Implement the `` NumArray `` class:

*   `` NumArray(int[] nums) `` Initializes the object with the integer array `` nums ``.
*   `` void update(int index, int val) `` __Updates__ the value of `` nums[index] `` to be `` val ``.
*   `` int sumRange(int left, int right) `` Returns the __sum__ of the elements of `` nums `` between indices `` left `` and `` right `` __inclusive__ (i.e. `` nums[left] + nums[left + 1] + ... + nums[right] ``).

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
<strong>Output</strong>
[null, 9, null, 8]

<strong>Explanation</strong>
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code>
*   `` -100 &lt;= nums[i] &lt;= 100 ``
*   `` 0 &lt;= index &lt; nums.length ``
*   `` -100 &lt;= val &lt;= 100 ``
*   `` 0 &lt;= left &lt;= right &lt; nums.length ``
*   At most <code>3 * 10<sup>4</sup></code> calls will be made to `` update `` and `` sumRange ``.