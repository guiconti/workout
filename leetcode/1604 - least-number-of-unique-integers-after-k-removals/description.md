Given an array of integers&nbsp;`` arr ``&nbsp;and an integer `` k ``.&nbsp;Find the _least number of unique integers_&nbsp;after removing __exactly__ `` k `` elements__.__

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>arr = [5,5,4], k = 1
<strong>Output: </strong>1
<strong>Explanation</strong>: Remove the single 4, only 5 is left.
</pre>

__Example 2:__

<pre>
<strong>Input: </strong>arr = [4,3,1,1,3,3,2], k = 3
<strong>Output: </strong>2
<strong>Explanation</strong>: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.</pre>

&nbsp;

__Constraints:__

*   `` 1 &lt;= arr.length&nbsp;&lt;= 10^5 ``
*   `` 1 &lt;= arr[i] &lt;= 10^9 ``
*   `` 0 &lt;= k&nbsp;&lt;= arr.length ``