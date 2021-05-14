A sequence of numbers is called an __arithmetic progression__ if the difference between any two consecutive elements is the same.

Given an array of numbers `` arr ``, return `` true `` _if the array can be rearranged to form an __arithmetic progression__. Otherwise, return_ `` false ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> arr = [3,5,1]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> arr = [1,2,4]
<strong>Output:</strong> false
<strong>Explanation: </strong>There is no way to reorder the elements to obtain an arithmetic progression.
</pre>

&nbsp;

__Constraints:__

*   `` 2 &lt;= arr.length &lt;= 1000 ``
*   <code>-10<sup>6</sup> &lt;= arr[i] &lt;= 10<sup>6</sup></code>