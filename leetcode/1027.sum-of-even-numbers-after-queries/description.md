We have an array `` A `` of integers, and an array `` queries ``&nbsp;of queries.

For the `` i ``-th&nbsp;query `` val =&nbsp;queries[i][0], index&nbsp;= queries[i][1] ``, we add 

<font face="monospace">val</font>

&nbsp;to `` A[index] ``.&nbsp; Then, the answer to the `` i ``-th query is the sum of the even values of `` A ``.

_(Here, the given `` index = queries[i][1] `` is a 0-based index, and each query permanently modifies the array `` A ``.)_

Return the answer to all queries.&nbsp; Your `` answer `` array should have&nbsp;`` answer[i] ``&nbsp;as&nbsp;the answer to the `` i ``-th query.

&nbsp;

__Example 1:__

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,2,3,4]</span>, queries = <span id="example-input-1-2">[[1,0],[-3,1],[-4,0],[2,3]]</span>
<strong>Output: </strong><span id="example-output-1">[8,6,2,4]</span>
<strong>Explanation: </strong>
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
</pre>

&nbsp;

__Note:__

1.   `` 1 &lt;= A.length &lt;= 10000 ``
2.   `` -10000 &lt;= A[i] &lt;= 10000 ``
3.   `` 1 &lt;= queries.length &lt;= 10000 ``
4.   `` -10000 &lt;= queries[i][0] &lt;= 10000 ``
5.   `` 0 &lt;= queries[i][1] &lt; A.length ``