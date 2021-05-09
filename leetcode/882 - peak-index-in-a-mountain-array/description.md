Let's call an array `` arr `` a __mountain__&nbsp;if the following properties hold:

*   `` arr.length &gt;= 3 ``
*   There exists some `` i `` with&nbsp;`` 0 &lt; i&nbsp;&lt; arr.length - 1 ``&nbsp;such that:	
    
    *   `` arr[0] &lt; arr[1] &lt; ... arr[i-1] &lt; arr[i]  ``
    *   `` arr[i] &gt; arr[i+1] &gt; ... &gt; arr[arr.length - 1] ``
    
    
    

Given an integer array `` arr `` that is __guaranteed__ to be&nbsp;a mountain, return any&nbsp;`` i ``&nbsp;such that&nbsp;`` arr[0] &lt; arr[1] &lt; ... arr[i - 1] &lt; arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1] ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> arr = [0,1,0]
<strong>Output:</strong> 1
</pre>

__Example 2:__

<pre><strong>Input:</strong> arr = [0,2,1,0]
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre><strong>Input:</strong> arr = [0,10,5,2]
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre><strong>Input:</strong> arr = [3,4,5,1]
<strong>Output:</strong> 2
</pre>

__Example 5:__

<pre><strong>Input:</strong> arr = [24,69,100,99,79,78,67,36,26,19]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

*   <code>3 &lt;= arr.length &lt;= 10<sup>4</sup></code>
*   <code>0 &lt;= arr[i] &lt;= 10<sup>6</sup></code>
*   `` arr `` is __guaranteed__ to be a mountain array.

&nbsp;
__Follow up:__ Finding the `` O(n) `` is straightforward, could you find an `` O(log(n)) `` solution?