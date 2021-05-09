You are given an array of `` n `` strings `` strs ``, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have `` strs = ["abcdef","uvwxyz"] `` and deletion indices `` {0, 2, 3} ``, then the final array after deletions is `` ["bef", "vyz"] ``.

Suppose we chose a set of deletion indices `` answer `` such that after deletions, the final array has its elements in __lexicographic__ order (i.e., `` strs[0] &lt;= strs[1] &lt;= strs[2] &lt;= ... &lt;= strs[n - 1] ``). Return _the minimum possible value of_ `` answer.length ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> strs = ["ca","bb","ac"]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] &lt;= strs[1] &lt;= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> strs = ["xc","yb","za"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
strs is already in lexicographic order, so we do not need to delete anything.
Note that the rows of strs are not necessarily in lexicographic order:
i.e., it is NOT necessarily true that (strs[0][0] &lt;= strs[0][1] &lt;= ...)
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> strs = ["zyx","wvu","tsr"]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We have to delete every column.
</pre>

&nbsp;

__Constraints:__

*   `` n == strs.length ``
*   `` 1 &lt;= n &lt;= 100 ``
*   `` 1 &lt;= strs[i].length &lt;= 100 ``
*   `` strs[i] `` consists of lowercase English letters.