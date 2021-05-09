Design a class to find&nbsp;the <code>k<sup>th</sup></code> largest element in a stream. Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.

Implement&nbsp;`` KthLargest ``&nbsp;class:

*   `` KthLargest(int k, int[] nums) ``&nbsp;Initializes the object with the integer `` k `` and the stream of integers `` nums ``.
*   `` int add(int val) ``&nbsp;Returns the element representing the <code>k<sup>th</sup></code> largest element in the stream.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
<strong>Output</strong>
[null, 4, 5, 5, 8, 8]

<strong>Explanation</strong>
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= k &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> &lt;= val &lt;= 10<sup>4</sup></code>
*   At most <code>10<sup>4</sup></code> calls will be made to `` add ``.
*   It is guaranteed that there will be at least `` k `` elements in the array when you search for the <code>k<sup>th</sup></code> element.