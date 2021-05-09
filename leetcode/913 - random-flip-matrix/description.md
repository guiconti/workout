You are given the number of rows `` n_rows ``&nbsp;and number of columns `` n_cols ``&nbsp;of a&nbsp;2D&nbsp;binary matrix&nbsp;where all values are initially 0.&nbsp;Write a function `` flip ``&nbsp;which chooses&nbsp;a 0 value&nbsp;<a href="https://en.wikipedia.org/wiki/Discrete_uniform_distribution" target="_blank">uniformly at random</a>,&nbsp;changes it to 1,&nbsp;and then returns the position `` [row.id, col.id] `` of that value. Also, write a function `` reset `` which sets all values back to 0.&nbsp;__Try to minimize the number of calls to system's Math.random()__ and optimize the time and&nbsp;space complexity.

Note:

1.   `` 1 &lt;= n_rows, n_cols&nbsp;&lt;= 10000 ``
2.   `` 0 &lt;= row.id &lt; n_rows `` and `` 0 &lt;= col.id &lt; n_cols ``
3.   `` flip ``&nbsp;will not be called when the matrix has no&nbsp;0 values left.
4.   the total number of calls to&nbsp;`` flip ``&nbsp;and `` reset ``&nbsp;will not exceed&nbsp;1000.

__Example 1:__

<pre>
<strong>Input: 
</strong><span id="example-input-1-1">["Solution","flip","flip","flip","flip"]
</span><span id="example-input-1-2">[[2,3],[],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-1">[null,[0,1],[1,2],[1,0],[1,1]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: 
</strong><span id="example-input-2-1">["Solution","flip","flip","reset","flip"]
</span><span id="example-input-2-2">[[1,2],[],[],[],[]]</span>
<strong>Output: </strong><span id="example-output-2">[null,[0,0],[0,1],null,[0,0]]</span></pre>
</div>

__Explanation of Input Syntax:__

The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments. `` Solution ``'s constructor&nbsp;has two arguments, `` n_rows `` and `` n_cols ``.&nbsp;`` flip ``&nbsp;and `` reset `` have&nbsp;no&nbsp;arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren't any.