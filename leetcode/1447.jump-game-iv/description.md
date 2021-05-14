Given an array of&nbsp;integers `` arr ``, you are initially positioned at the first index of the array.

In one step you can jump from index `` i `` to index:

*   `` i + 1 `` where:&nbsp;`` i + 1 &lt; arr.length ``.
*   `` i - 1 `` where:&nbsp;`` i - 1 &gt;= 0 ``.
*   `` j `` where: `` arr[i] == arr[j] `` and `` i != j ``.

Return _the minimum number of steps_ to reach the __last index__ of the array.

Notice that you can not jump outside of the array at any time.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [100,-23,-23,404,100,23,23,23,3,404]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You need three jumps from index 0 --&gt; 4 --&gt; 3 --&gt; 9. Note that index 9 is the last index of the array.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [7]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Start index is the last index. You don't need to jump.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [7,6,9,6,9,6,9,7]
<strong>Output:</strong> 1
<strong>Explanation:</strong> You can jump directly from index 0 to index 7 which is last index of the array.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> arr = [6,1,9]
<strong>Output:</strong> 2
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> arr = [11,22,7,7,7,7,7,7,7,22,13]
<strong>Output:</strong> 3
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code>
*   <code>-10<sup>8</sup> &lt;= arr[i] &lt;= 10<sup>8</sup></code>