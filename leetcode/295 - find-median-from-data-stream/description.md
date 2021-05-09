The __median__ is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

*   For example, for `` arr = [2,3,4] ``, the median is `` 3 ``.
*   For example, for `` arr = [2,3] ``, the median is `` (2 + 3) / 2 = 2.5 ``.

Implement the MedianFinder class:

*   `` MedianFinder() `` initializes the `` MedianFinder `` object.
*   `` void addNum(int num) `` adds the integer `` num `` from the data stream to the data structure.
*   `` double findMedian() `` returns the median of all elements so far. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.

&nbsp;

__Example 1:__

<pre>
<strong>Input</strong>
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
<strong>Output</strong>
[null, null, null, 1.5, null, 2.0]

<strong>Explanation</strong>
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
</pre>

&nbsp;

__Constraints:__

*   <code>-10<sup>5</sup> &lt;= num &lt;= 10<sup>5</sup></code>
*   There will be at least one element in the data structure before calling `` findMedian ``.
*   At most <code>5 * 10<sup>4</sup></code> calls will be made to `` addNum `` and `` findMedian ``.

&nbsp;

__Follow up:__

*   If all integer numbers from the stream are in the range `` [0, 100] ``, how would you optimize your solution?
*   If `` 99% `` of all integer numbers from the stream are in the range `` [0, 100] ``, how would you optimize your solution?