Given an array `` arr ``&nbsp;of positive integers&nbsp;sorted in a __strictly increasing order__, and an integer <code><font face="monospace">k</font></code>.

_Find the _

<font face="monospace"><code>k<sup>th</sup></code></font>

_&nbsp;positive integer that is missing from this array._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [2,3,4,7,11], k = 5
<strong>Output:</strong> 9
<strong>Explanation: </strong>The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5<sup>th</sup>&nbsp;missing positive integer is 9.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,2,3,4], k = 2
<strong>Output:</strong> 6
<strong>Explanation: </strong>The missing positive integers are [5,6,7,...]. The 2<sup>nd</sup> missing positive integer is 6.
</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length &lt;= 1000 ``
*   `` 1 &lt;= arr[i] &lt;= 1000 ``
*   `` 1 &lt;= k &lt;= 1000 ``
*   `` arr[i] &lt; arr[j] `` for `` 1 &lt;= i &lt; j &lt;= arr.length ``