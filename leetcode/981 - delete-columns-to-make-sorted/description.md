You are given an array of `` n `` strings `` strs ``, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, `` strs = ["abc", "bce", "cae"] `` can be arranged as:

<pre>
abc
bce
cae
</pre>

You want to __delete__ the columns that are __not sorted lexicographically__. In the above example (0-indexed), columns 0 (`` 'a' ``, `` 'b' ``, `` 'c' ``) and 2 (`` 'c' ``, `` 'e' ``, `` 'e' ``) are sorted while column 1 (`` 'b' ``, `` 'c' ``, `` 'a' ``) is not, so you would delete column 1.

Return _the number of columns that you will delete_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> strs = ["cba","daf","ghi"]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> strs = ["a","b"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> strs = ["zyx","wvu","tsr"]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
</pre>

&nbsp;

__Constraints:__

*   `` n == strs.length ``
*   `` 1 &lt;= n &lt;= 100 ``
*   `` 1 &lt;= strs[i].length &lt;= 1000 ``
*   `` strs[i] `` consists of lowercase English letters.