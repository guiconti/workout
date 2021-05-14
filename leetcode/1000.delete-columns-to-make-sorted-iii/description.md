You are given an array of `` n `` strings `` strs ``, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have `` strs = ["abcdef","uvwxyz"] `` and deletion indices `` {0, 2, 3} ``, then the final array after deletions is `` ["bef", "vyz"] ``.

Suppose we chose a set of deletion indices `` answer `` such that after deletions, the final array has __every string (row) in lexicographic__ order. (i.e., `` (strs[0][0] &lt;= strs[0][1] &lt;= ... &lt;= strs[0][strs[0].length - 1]) ``, and `` (strs[1][0] &lt;= strs[1][1] &lt;= ... &lt;= strs[1][strs[1].length - 1]) ``, and so on). Return _the minimum possible value of_ `` answer.length ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> strs = ["babca","bbazb"]
<strong>Output:</strong> 3
<strong>Explanation:</strong> After deleting columns 0, 1, and 4, the final array is strs = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. strs[0][0] &lt;= strs[0][1] and strs[1][0] &lt;= strs[1][1]).
Note that strs[0] &gt; strs[1] - the array strs is not necessarily in lexicographic order.</pre>

__Example 2:__

<pre>
<strong>Input:</strong> strs = ["edcba"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> If we delete less than 4 columns, the only row will not be lexicographically sorted.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> strs = ["ghi","def","abc"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All rows are already lexicographically sorted.
</pre>

&nbsp;

__Constraints:__

*   `` n == strs.length ``
*   `` 1 &lt;= n &lt;= 100 ``
*   `` 1 &lt;= strs[i].length &lt;= 100 ``
*   `` strs[i] `` consists of lowercase English letters.

*   &nbsp;