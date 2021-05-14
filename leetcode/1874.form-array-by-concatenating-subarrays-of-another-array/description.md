You are given a 2D integer array `` groups `` of length `` n ``. You are also given an integer array `` nums ``.

You are asked if you can choose `` n `` __disjoint __subarrays from the array `` nums `` such that the <code>i<sup>th</sup></code> subarray is equal to `` groups[i] `` (__0-indexed__), and if `` i &gt; 0 ``, the <code>(i-1)<sup>th</sup></code> subarray appears __before__ the <code>i<sup>th</sup></code> subarray in `` nums `` (i.e. the subarrays must be in the same order as `` groups ``).

Return `` true `` _if you can do this task, and_ `` false `` _otherwise_.

Note that the subarrays are __disjoint__ if and only if there is no index `` k `` such that `` nums[k] `` belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> You can choose the 0<sup>th</sup> subarray as [1,-1,0,<u><strong>1,-1,-1</strong></u>,3,-2,0] and the 1<sup>st</sup> one as [1,-1,0,1,-1,-1,<u><strong>3,-2,0</strong></u>].
These subarrays are disjoint as they share no common nums[k] element.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]
<strong>Output:</strong> false
<strong>Explanation: </strong>Note that choosing the subarrays [<u><strong>1,2,3,4</strong></u>,10,-2] and [1,2,3,4,<u><strong>10,-2</strong></u>] is incorrect because they are not in the same order as in groups.
[10,-2] must come before [1,2,3,4].
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]
<strong>Output:</strong> false
<strong>Explanation: </strong>Note that choosing the subarrays [7,7,<u><strong>1,2,3</strong></u>,4,7,7] and [7,7,1,2,<u><strong>3,4</strong></u>,7,7] is invalid because they are not disjoint.
They share a common elements nums[4] (0-indexed).
</pre>

&nbsp;

__Constraints:__

*   `` groups.length == n ``
*   <code>1 &lt;= n &lt;= 10<sup>3</sup></code>
*   <code>1 &lt;= groups[i].length, sum(groups[i].length) &lt;= 10<sup><span style="font-size: 10.8333px;">3</span></sup></code>
*   <code>1 &lt;= nums.length &lt;= 10<sup>3</sup></code>
*   <code>-10<sup>7</sup> &lt;= groups[i][j], nums[k] &lt;= 10<sup>7</sup></code>