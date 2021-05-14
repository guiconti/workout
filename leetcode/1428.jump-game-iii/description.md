Given an array of non-negative integers `` arr ``, you are initially positioned at `` start ``&nbsp;index of the array. When you are at index `` i ``, you can jump&nbsp;to `` i + arr[i] `` or `` i - arr[i] ``, check if you can reach to __any__ index with value 0.

Notice that you can not jump outside of the array at any time.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [4,2,3,0,3,1,2], start = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> 
All possible ways to reach at index 3 with value 0 are: 
index 5 -&gt; index 4 -&gt; index 1 -&gt; index 3 
index 5 -&gt; index 6 -&gt; index 4 -&gt; index 1 -&gt; index 3 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [4,2,3,0,3,1,2], start = 0
<strong>Output:</strong> true 
<strong>Explanation: 
</strong>One possible way to reach at index 3 with value 0 is: 
index 0 -&gt; index 4 -&gt; index 1 -&gt; index 3
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> arr = [3,0,2,1,2], start = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>There is no way to reach at index 1 with value 0.
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code>
*   `` 0 &lt;= arr[i] &lt;&nbsp;arr.length ``
*   `` 0 &lt;= start &lt; arr.length ``