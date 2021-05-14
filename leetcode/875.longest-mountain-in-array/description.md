You may recall that an array `` arr `` is a __mountain array__ if and only if:

*   `` arr.length &gt;= 3 ``
*   There exists some index `` i `` (__0-indexed__) with `` 0 &lt; i &lt; arr.length - 1 `` such that:	
    
    *   `` arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i] ``
    *   `` arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1] ``
    
    
    

Given an integer array `` arr ``,&nbsp;return _the length of the longest subarray, which is a mountain_.&nbsp;Return `` 0 `` if there is no mountain subarray.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [2,1,4,7,3,2,5]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The largest mountain is [1,4,7,3,2] which has length 5.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [2,2,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no mountain.
</pre>

&nbsp;

__Constraints:__

*   <code>1&nbsp;&lt;= arr.length &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code>

&nbsp;

__Follow up:__

*   Can you solve it using only one pass?
*   Can you solve it in `` O(1) `` space?