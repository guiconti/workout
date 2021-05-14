You are given two integer arrays, `` source `` and `` target ``, both of length `` n ``. You are also given an array `` allowedSwaps `` where each <code>allowedSwaps[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you are allowed to swap the elements at index <code>a<sub>i</sub></code> and index <code>b<sub>i</sub></code> __(0-indexed)__ of array `` source ``. Note that you can swap elements at a specific pair of indices __multiple__ times and in __any__ order.

The __Hamming distance__ of two arrays of the same length, `` source `` and `` target ``, is the number of positions where the elements are different. Formally, it is the number of indices `` i `` for `` 0 &lt;= i &lt;= n-1 `` where `` source[i] != target[i] `` __(0-indexed)__.

Return _the __minimum Hamming distance__ of _`` source ``_ and _`` target ``_ after performing __any__ amount of swap operations on array _`` source ``_._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> source can be transformed the following way:
- Swap indices 0 and 1: source = [<u>2</u>,<u>1</u>,3,4]
- Swap indices 2 and 3: source = [2,1,<u>4</u>,<u>3</u>]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

*   `` n == source.length == target.length ``
*   <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
*   <code>1 &lt;= source[i], target[i] &lt;= 10<sup>5</sup></code>
*   <code>0 &lt;= allowedSwaps.length &lt;= 10<sup>5</sup></code>
*   `` allowedSwaps[i].length == 2 ``
*   <code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>