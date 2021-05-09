Given an array of integers arr, find the sum of `` min(b) ``, where `` b `` ranges over every (contiguous) subarray of `` arr ``. Since the answer may be large, return the answer __modulo__ <code>10<sup>9</sup> + 7</code>.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,1,2,4]
<strong>Output:</strong> 17
<strong>Explanation:</strong> 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [11,81,94,43,3]
<strong>Output:</strong> 444
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code>
*   <code>1 &lt;= arr[i] &lt;= 3 * 10<sup>4</sup></code>