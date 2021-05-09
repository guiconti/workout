Given an array of integers `` arr ``, return `` true `` if we can partition the array into three __non-empty__ parts with equal sums.

Formally, we can partition the array if we can find indexes `` i + 1 &lt; j `` with `` (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1]) ``

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [0,2,1,-6,6,-7,9,1,2,0,1]
<strong>Output:</strong> true
<strong>Explanation: </strong>0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [0,2,1,-6,6,7,9,-1,2,0,1]
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [3,3,6,5,-2,2,5,1,-9,4]
<strong>Output:</strong> true
<strong>Explanation: </strong>3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
</pre>

&nbsp;

__Constraints:__

*   <code>3 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> &lt;= arr[i] &lt;= 10<sup>4</sup></code>