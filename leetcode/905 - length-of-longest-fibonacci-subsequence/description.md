A sequence <code>X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>n</sub></code> is _Fibonacci-like_ if:

*   `` n &gt;= 3 ``
*   <code>X<sub>i</sub> + X<sub>i+1</sub> = X<sub>i+2</sub></code> for all `` i + 2 &lt;= n ``

Given a __strictly increasing__ array `` arr `` of positive integers forming a sequence, return the __length__ of the longest Fibonacci-like subsequence of `` arr ``. If one does not exist, return `` 0 ``.

_A subsequence is derived from another sequence `` arr `` by deleting any number of elements (including none) from `` arr ``, without changing the order of the remaining elements. For example, `` [3, 5, 8] `` is a subsequence of `` [3, 4, 5, 6, 7, 8] ``._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,6,7,8]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest subsequence that is fibonacci-like: [1,2,3,5,8].</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,3,7,11,12,14,18]
<strong>Output:</strong> 3
<strong>Explanation</strong>:<strong> </strong>The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].</pre>

&nbsp;

__Constraints:__

*   `` 3 &lt;= arr.length &lt;= 1000 ``
*   <code>1 &lt;= arr[i] &lt; arr[i + 1] &lt;= 10<sup>9</sup></code>