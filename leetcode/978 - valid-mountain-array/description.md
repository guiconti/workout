Given an array of integers `` arr ``, return _`` true `` if and only if it is a valid mountain array_.

Recall that arr is a mountain array if and only if:

*   `` arr.length &gt;= 3 ``
*   There exists some `` i `` with `` 0 &lt; i &lt; arr.length - 1 `` such that:	
    
    *   `` arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i]  ``
    *   `` arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1] ``
    
    
    

<img src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" width="500"/>

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> arr = [2,1]
<strong>Output:</strong> false
</pre>

__Example 2:__

<pre><strong>Input:</strong> arr = [3,5,5]
<strong>Output:</strong> false
</pre>

__Example 3:__

<pre><strong>Input:</strong> arr = [0,3,2,1]
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

*   <code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code>