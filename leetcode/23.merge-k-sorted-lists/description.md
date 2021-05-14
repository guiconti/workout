You are given an array of `` k `` linked-lists `` lists ``, each linked-list is sorted in ascending order.

_Merge all the linked-lists into one sorted linked-list and return it._

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
merging them into one sorted list:
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

*   `` k == lists.length ``
*   `` 0 &lt;= k &lt;= 10^4 ``
*   `` 0 &lt;= lists[i].length &lt;= 500 ``
*   `` -10^4 &lt;= lists[i][j] &lt;= 10^4 ``
*   `` lists[i] `` is sorted in __ascending order__.
*   The sum of `` lists[i].length `` won't exceed `` 10^4 ``.