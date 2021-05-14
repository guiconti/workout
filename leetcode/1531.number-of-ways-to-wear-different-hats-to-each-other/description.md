There are&nbsp;`` n `` people&nbsp;and 40 types of hats labeled from 1 to 40.

Given a list of list of integers `` hats ``, where `` hats[i] ``&nbsp;is a list of all hats preferred&nbsp;by the <code data-stringify-type="code">i-th</code> person.

Return the number of ways that the n people wear different hats to each other.

Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;`` 10^9 + 7 ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> hats = [[3,4],[4,5],[5]]
<strong>Output:</strong> 1
<strong>Explanation: </strong>There is only one way to choose hats given the conditions. 
First person choose hat 3, Second person choose hat 4 and last one hat 5.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> hats = [[3,5,1],[3,5]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>There are 4 ways to choose hats
(3,5), (5,3), (1,3) and (1,5)
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
<strong>Output:</strong> 24
<strong>Explanation: </strong>Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
<strong>Output:</strong> 111
</pre>

&nbsp;

__Constraints:__

*   `` n == hats.length ``
*   `` 1 &lt;= n &lt;= 10 ``
*   `` 1 &lt;= hats[i].length &lt;= 40 ``
*   `` 1 &lt;= hats[i][j] &lt;= 40 ``
*   `` hats[i] `` contains a list of __unique__ integers.