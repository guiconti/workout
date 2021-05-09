There are `` n `` soldiers standing in a line. Each soldier is assigned a __unique__ `` rating `` value.

You have to form a team of 3 soldiers amongst them under the following rules:

*   Choose 3 soldiers with index (`` i ``, `` j ``, `` k ``) with rating (`` rating[i] ``, `` rating[j] ``, `` rating[k] ``).
*   A team is valid if: (`` rating[i] &lt; rating[j] &lt; rating[k] ``) or (`` rating[i] &gt; rating[j] &gt; rating[k] ``) where (`` 0 &lt;= i &lt; j &lt; k &lt; n ``).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> rating = [2,5,3,4,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> rating = [2,1,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> We can't form any team given the conditions.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> rating = [1,2,3,4]
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

*   `` n == rating.length ``
*   `` 3 &lt;= n &lt;= 1000 ``
*   <code>1 &lt;= rating[i] &lt;= 10<sup>5</sup></code>
*   All the integers in `` rating `` are __unique__.